import argparse
# Change the import here to get the correct model 
# (async or without)
import asyncio
from tot.methods.bfs_async import solve_async
# from tot.methods.bfs import solve

from tot.tasks.game24 import Game24Task

args = argparse.Namespace(backend='gpt-4o-mini', 
                          temperature=0.7, 
                          task='game24', 
                          naive_run=False, 
                          prompt_sample=None, 
                          method_generate='propose', 
                          method_evaluate='value', 
                          method_select='greedy', 
                          n_generate_sample=1, 
                          n_evaluate_sample=3, 
                          n_select_sample=5)

task = Game24Task()

async def main():
  task = Game24Task()
  for i in range(10):
    print(f"Task {900+i}")
    ys, _ = await solve_async(args, task, 900+i)
    print(ys[0])

if __name__ == "__main__":
  asyncio.run(main())