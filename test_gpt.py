from tot.models import gpt, gpt_usage

# Example: Generate a single creative idea
idea = gpt("Suggest a name for a new AI research project focused on logic.")
print(f"Suggestion: {idea[0]}")

# Example: Generate multiple independent samples (n=3)
# This is used in bfs.py to get multiple candidate solutions
options = gpt("Write a 1-sentence math riddle.", n=3, temperature=0.9)
for i, opt in enumerate(options):
    print(f"Option {i+1}: {opt}")

# Check the bill
usage = gpt_usage(backend="gpt-4o-mini")
print(f"Tokens Used: {usage['prompt_tokens']} prompt, {usage['completion_tokens']} completion")
print(f"Estimated Cost: ${usage['cost']:.4f}")