import os
from openai import OpenAI
import backoff 

# Initialize client (it automatically finds OPENAI_API_KEY)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE") or None
)

completion_tokens = prompt_tokens = 0

# Updated to modern Exception class
@backoff.on_exception(backoff.expo, Exception)
def completions_with_backoff(**kwargs):
    return client.chat.completions.create(**kwargs)

def gpt(prompt, model="gpt-4o-mini", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    messages = [{"role": "user", "content": prompt}]
    return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)
    
def chatgpt(messages, model="gpt-4o-mini", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    global completion_tokens, prompt_tokens
    print(f"Sending request to {model}...")
    # print(messages)
    
    # Modern response handling
    res = completions_with_backoff(
        model=model, 
        messages=messages, 
        temperature=temperature, 
        max_tokens=max_tokens, 
        n=n, 
        stop=stop
    )
    
    # Access attributes directly (no longer a dictionary)
    outputs = [choice.message.content for choice in res.choices]
    
    completion_tokens += res.usage.completion_tokens
    prompt_tokens += res.usage.prompt_tokens
    
    print(f"Received {len(outputs)} responses.")
    # print(outputs)

    # Track usage
    usage = gpt_usage(backend="gpt-4o-mini")
    print(f"Tokens Used: {usage['prompt_tokens']} prompt, {usage['completion_tokens']} completion")
    print(f"Estimated Cost: ${usage['cost']:.4f}")

    return outputs

def gpt_usage(backend="gpt-4o-mini"):
    # Updated pricing for gpt-4o-mini (approx $0.15/1M input, $0.60/1M output)
    cost = (prompt_tokens / 1_000_000 * 0.15) + (completion_tokens / 1_000_000 * 0.60)
    return {"completion_tokens": completion_tokens, "prompt_tokens": prompt_tokens, "cost": cost}