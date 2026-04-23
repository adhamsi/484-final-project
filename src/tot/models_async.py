import os
import asyncio
import backoff
from openai import AsyncOpenAI


completion_tokens = 0
prompt_tokens = 0

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE") or None
)

# We can tune this based on how many async calls we want to make
semaphore = asyncio.Semaphore(5)


@backoff.on_exception(backoff.expo, Exception)
async def completions_with_backoff(**kwargs):
    return await client.chat.completions.create(**kwargs)


async def chatgpt_async(messages, model="gpt-4o-mini", temperature=0.7, max_tokens=1000, n=1, stop=None):
    global completion_tokens, prompt_tokens

    async with semaphore:
        print(f"Sending request to {model}...")

        res = await completions_with_backoff(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            n=n,
            stop=stop
        )

    outputs = [choice.message.content for choice in res.choices]

    # Track usage
    completion_tokens += res.usage.completion_tokens
    prompt_tokens += res.usage.prompt_tokens

    print(f"Received {len(outputs)} responses.")

    usage = gpt_usage()
    print(f"Tokens Used: {usage['prompt_tokens']} prompt, {usage['completion_tokens']} completion")
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