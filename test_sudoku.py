import argparse
# Change the import here to get the correct model 
# (async or without)
import asyncio
# from tot.methods.bfs_async import solve_async
from tot.methods.bfs import solve
from tot.tasks.sudoku import SudokuTask


args = argparse.Namespace(backend='gpt-4o-mini', 
                          temperature=0.7, 
                          task='sudoku', 
                          naive_run=False, 
                          prompt_sample=None, 
                          method_generate='propose', # Should be propose, gets sequential thoughts (used in Game of 24)
                          method_evaluate='value', 
                          method_select='greedy', 
                          n_generate_sample=1, 
                          n_evaluate_sample=3, 
                          n_select_sample=5)

# async def main():
#   task = SudokuTask()
#   for i in range(10):
#     print(f"Task {0 + i}")
#     ys, _ = await solve_async(args, task, 0 + i)
#     print(ys[0])

def main():
  task = SudokuTask()
  for i in range(10):
    print(f"Task {0 + i}")
    ys, _ = solve(args, task, 0 + i)
    print(ys[0])

if __name__ == "__main__":
  asyncio.run(main())