import argparse
# Change the import here to get the correct model 
# (async or without)
import asyncio
from tot.methods.bfs_async import solve_async
# from tot.methods.bfs import solve
# from tot.methods.bfs import naive_solve


from tot.tasks.game24 import Game24Task

args = argparse.Namespace(backend='gpt-4o-mini', 
                          temperature=.7, 
                          task='game24', 
                          naive_run=False, #if True, run naive IO/CoT sampling instead of ToT + BFS.
                          prompt_sample=None, # (choices=[``standard``, ``cot``]): sampling prompt
                          method_generate='propose', # (choices=[``sample``, ``propose``]): thought generator, whether 
                          # to sample independent thoughts (used in Creative Writing) or propose sequential thoughts (used in Game of 24)
                          method_evaluate='value', # (choices=[``value``, ``vote``]): state evaluator, whether to use the value states independently 
                          # (used in Game of 24) or vote on states together (used in Creative Writing)
                          method_select='greedy', 
                          n_generate_sample=1, # number of times to prompt for thought generation
                          n_evaluate_sample=3, # number of times to prompt for state evaluation
                          n_select_sample=3) # number of states to keep from each step (i.e. ``b`` in the paper's ToT + BFS algorithm)

task = Game24Task()

async def main():
  task = Game24Task()
  for i in range(10):
    print(f"Task {900+i}")
    ys, _ = await solve_async(args, task, 900+i)
    print(ys[0])

if __name__ == "__main__":
  asyncio.run(main())



  