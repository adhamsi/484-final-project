import asyncio
import itertools
import numpy as np
from tot.models_async import gpt_async, gpt_usage
from tot.models_async import debugging_on

async def get_value(task, x, y, n_evaluate_sample, cache_value=True):
    value_prompt = task.value_prompt_wrap(x, y)

    if cache_value and value_prompt in task.value_cache:
        return task.value_cache[value_prompt]

    if debugging_on:
        print(f"DEBUG: Evaluating node value with {n_evaluate_sample} samples...")

    value_outputs = await gpt_async(value_prompt, n=n_evaluate_sample)
    value = task.value_outputs_unwrap(x, y, value_outputs)

    if cache_value:
        task.value_cache[value_prompt] = value

    return value


async def get_values(task, x, ys, n_evaluate_sample, cache_value=True):
    local_cache = {}

    async def worker(y):
        if y in local_cache:
            return local_cache[y]

        val = await get_value(task, x, y, n_evaluate_sample, cache_value)
        local_cache[y] = val
        return val

    return await asyncio.gather(*[worker(y) for y in ys])


async def get_votes(task, x, ys, n_evaluate_sample):
    if debugging_on:
        print(f"DEBUG: Getting votes for {len(ys)} candidates...")
        
    vote_prompt = task.vote_prompt_wrap(x, ys)
    vote_outputs = await gpt_async(vote_prompt, n=n_evaluate_sample)
    return task.vote_outputs_unwrap(vote_outputs, len(ys))


async def get_proposals(task, x, y):
    if debugging_on:
        print(f"DEBUG: Generating proposals for: {y.strip()}")
        
    propose_prompt = task.propose_prompt_wrap(x, y)
    proposals = (await gpt_async(propose_prompt, n=1))[0].split('\n')
    return [y + p + '\n' for p in proposals]


async def get_samples(task, x, y, n_generate_sample, prompt_sample, stop):
    if debugging_on:
        print(f"DEBUG: Sampling {n_generate_sample} outputs ({prompt_sample})")

    if prompt_sample == 'standard':
        prompt = task.standard_prompt_wrap(x, y)
    elif prompt_sample == 'cot':
        prompt = task.cot_prompt_wrap(x, y)
    else:
        raise ValueError(prompt_sample)

    samples = await gpt_async(prompt, n=n_generate_sample, stop=stop)
    return [y + s for s in samples]


async def solve_async(args, task, idx):
    x = task.get_input(idx)

    if True:
        print(f"\n--- STARTING SOLVE | {x} ---")

    ys = ['']
    infos = []

    for step in range(task.steps):
        if True:
            print(f"\n== STEP {step+1}/{task.steps} ==")

        if args.method_generate == 'sample':
            new_ys_nested = await asyncio.gather(*[
                get_samples(task, x, y, args.n_generate_sample, args.prompt_sample, task.stops[step])
                for y in ys
            ])
        else:
            new_ys_nested = await asyncio.gather(*[
                get_proposals(task, x, y)
                for y in ys
            ])

        new_ys = list(itertools.chain(*new_ys_nested))

        if debugging_on:
            print(f"Generated {len(new_ys)} candidates")

        if args.method_evaluate == 'vote':
            values = await get_votes(task, x, new_ys, args.n_evaluate_sample)
        else:
            values = await get_values(task, x, new_ys, args.n_evaluate_sample)

        ids = list(range(len(new_ys)))

        if args.method_select == 'sample':
            probs = np.array(values) / (sum(values) + 1e-9)
            selected = np.random.choice(ids, size=args.n_select_sample, p=probs)
        else:
            selected = sorted(ids, key=lambda i: values[i], reverse=True)[:args.n_select_sample]

        ys = [new_ys[i] for i in selected]

        if debugging_on:
            print(f"Top value: {max(values) if values else 0}")

        infos.append({"step": step, "x": x, "ys": ys, "new_ys": new_ys, "values": values})

    if debugging_on:
        print("\nFINAL:", ys)

    if True:
        usage = gpt_usage()
        print(f"Tokens Used: {usage['prompt_tokens']} prompt, {usage['completion_tokens']} completion")
        print(f"Estimated Cost: ${usage['cost']:.4f}")
        
    return ys, {"steps": infos}


def solve(args, task, idx):
    return asyncio.run(solve_async(args, task, idx))