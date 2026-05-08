import os
import asyncio
import backoff
from openai import AsyncOpenAI

# Global debugging toggle
debugging_on = True

completion_tokens = 0
prompt_tokens = 0

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE") or None
)

# We can tune this based on how many async calls we want to make
semaphore = asyncio.Semaphore(2)


@backoff.on_exception(backoff.expo, Exception)
async def completions_with_backoff(**kwargs):
    return await client.chat.completions.create(**kwargs)


async def chatgpt_async(messages, model="gpt-5-mini", temperature=0.7, max_tokens=1000, n=1, stop=None):
    global completion_tokens, prompt_tokens
    print("hi")
    print(messages)

    # Old API, chat completions

    # async with semaphore:
    #     if debugging_on:
    #         print(f"Sending request to {model}...")

    #     res = await completions_with_backoff(
    #         model=model,
    #         messages=messages,
    #         temperature=temperature,
    #         max_completion_tokens=max_tokens,
    #         n=n,
    #         stop=stop
    #     )

    # This works with Responses API, so 5 and beyond
    async with semaphore:
        res = await client.responses.create(
            model=model,
            input=messages,
            # max_output_tokens=max_tokens, wrong way to set? 
        )


    print("Output BEG")
    print(res)
    print("Output END")


    outputs = res.output_text # THIS NEEDS TO BE PARSED

    print(outputs)

    completion_tokens += getattr(res.usage, "output_tokens", 0)
    prompt_tokens += getattr(res.usage, "input_tokens", 0)

    if debugging_on:
        print(f"Received {len(outputs)} responses.")
        usage = gpt_usage()
        print(f"Tokens Used: {prompt_tokens} prompt, {completion_tokens} completion")
        print(f"Estimated Cost: ${usage['cost']:.4f}")

    return outputs


async def gpt_async(prompt, **kwargs):
    messages = [{"role": "user", "content": prompt}]
    return await chatgpt_async(messages, **kwargs)


def gpt_usage():
    cost = (prompt_tokens / 1_000_000 * 0.15) + (completion_tokens / 1_000_000 * 0.60)
    return {
        "completion_tokens": completion_tokens,
        "prompt_tokens": prompt_tokens,
        "cost": cost
    }