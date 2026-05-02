# draft for input for 9x9 sudoku

standard_prompt = '''
Solve a 9x9 sudoku puzzle. Given an input of a 9x9 array, where each 0 entry corresponds to a missing value, generate an output of a completed 9x9 sudoku array.



Input:

[0, 0, 0, 0, 8, 9, 5, 7, 4]
[7, 8, 2, 6, 0, 4, 0, 0, 0]
[5, 4, 9, 7, 0, 0, 8, 2, 6]
[0, 7, 1, 9, 2, 3, 4, 0, 8]
[0, 0, 0, 0, 7, 0, 6, 0, 1]
[0, 0, 4, 0, 1, 0, 2, 0, 7]
[1, 2, 3, 8, 0, 7, 0, 6, 5]
[4, 6, 0, 3, 9, 5, 0, 0, 0]
[9, 5, 0, 1, 0, 0, 7, 0, 3]

Output:

[3, 1, 6, 2, 8, 9, 5, 7, 4]
[7, 8, 2, 6, 5, 4, 3, 1, 9]
[5, 4, 9, 7, 3, 1, 8, 2, 6]
[6, 7, 1, 9, 2, 3, 4, 5, 8]
[2, 9, 5, 4, 7, 8, 6, 3, 1]
[8, 3, 4, 5, 1, 6, 2, 9, 7]
[1, 2, 3, 8, 4, 7, 9, 6, 5]
[4, 6, 7, 3, 9, 5, 1, 8, 2]
[9, 5, 8, 1, 6, 2, 7, 4, 3]



Input:

[0, 0, 5, 9, 0, 0, 2, 0, 8]
[7, 0, 8, 3, 0, 0, 4, 6, 0]
[0, 0, 0, 1, 4, 0, 0, 0, 0]
[0, 0, 4, 6, 0, 7, 5, 9, 0]
[0, 0, 0, 2, 0, 0, 6, 7, 0]
[6, 5, 0, 4, 0, 0, 1, 8, 0]
[0, 7, 2, 8, 0, 0, 9, 5, 0]
[5, 0, 6, 0, 2, 9, 8, 0, 1]
[8, 0, 0, 5, 6, 0, 3, 0, 7]

Output:

[3, 4, 5, 9, 7, 6, 2, 1, 8]
[7, 1, 8, 3, 5, 2, 4, 6, 9]
[2, 6, 9, 1, 4, 8, 7, 3, 5]
[1, 2, 4, 6, 8, 7, 5, 9, 3]
[9, 8, 3, 2, 1, 5, 6, 7, 4]
[6, 5, 7, 4, 9, 3, 1, 8, 2]
[4, 7, 2, 8, 3, 1, 9, 5, 6]
[5, 3, 6, 7, 2, 9, 8, 4, 1]
[8, 9, 1, 5, 6, 4, 3, 2, 7]



Input:

[6, 5, 0, 0, 3, 8, 0, 7, 4]
[3, 0, 0, 0, 0, 4, 8, 0, 1]
[8, 2, 0, 7, 0, 0, 0, 5, 9]
[5, 0, 9, 0, 0, 1, 4, 0, 7]
[7, 4, 3, 6, 0, 5, 0, 9, 8]
[0, 0, 0, 0, 0, 9, 0, 3, 0]
[0, 8, 0, 5, 0, 0, 0, 4, 0]
[4, 0, 0, 0, 6, 0, 0, 0, 5]
[9, 0, 0, 8, 4, 7, 6, 1, 0]

Output: 

[6, 5, 1, 9, 3, 8, 2, 7, 4]            
[3, 9, 7, 2, 5, 4, 8, 6, 1]            
[8, 2, 4, 7, 1, 6, 3, 5, 9]           
[5, 6, 9, 3, 8, 1, 4, 2, 7]             
[7, 4, 3, 6, 2, 5, 1, 9, 8]            
[2, 1, 8, 4, 7, 9, 5, 3, 6]            
[1, 8, 6, 5, 9, 2, 7, 4, 3]           
[4, 7, 2, 1, 6, 3, 9, 8, 5]            
[9, 3, 5, 8, 4, 7, 6, 1, 2]            



Input:

[9, 0, 1, 8, 6, 7, 0, 0, 0]            
[8, 0, 0, 3, 9, 5, 1, 0, 0]            
[3, 5, 0, 0, 2, 0, 6, 8, 9]
[0, 0, 0, 0, 0, 1, 0, 2, 8]
[7, 0, 2, 0, 8, 0, 4, 3, 5]
[5, 8, 9, 0, 3, 2, 0, 6, 1]
[0, 7, 5, 0, 0, 8, 3, 0, 0]
[2, 3, 4, 9, 0, 6, 8, 1, 7]
[0, 0, 8, 7, 1, 0, 5, 0, 2]


Output:

[9, 4, 1, 8, 6, 7, 2, 5, 3]
[8, 2, 6, 3, 9, 5, 1, 7, 4]
[3, 5, 7, 1, 2, 4, 6, 8, 9]
[4, 6, 3, 5, 7, 1, 9, 2, 8]
[7, 1, 2, 6, 8, 9, 4, 3, 5]
[5, 8, 9, 4, 3, 2, 7, 6, 1]
[1, 7, 5, 2, 4, 8, 3, 9, 6]
[2, 3, 4, 9, 5, 6, 8, 1, 7]
[6, 9, 8, 7, 1, 3, 5, 4, 2]



Input:

[0, 4, 8, 6, 1, 0, 0, 0, 7]
[0, 0, 0, 0, 0, 0, 0, 1, 6]
[3, 6, 0, 7, 9, 5, 0, 0, 0]
[0, 9, 0, 0, 3, 0, 7, 2, 0]
[7, 8, 6, 0, 2, 4, 1, 9, 3]
[1, 0, 2, 8, 0, 0, 0, 6, 5]
[0, 0, 3, 4, 0, 0, 0, 0, 0]
[9, 0, 3, 0, 0, 0, 0, 0, 0]
[8, 0, 7, 0, 0, 0, 6, 3, 4]

Output:

[2, 4, 8, 6, 1, 3, 9, 5, 7]
[5, 7, 9, 2, 4, 8, 3, 1, 6]
[3, 6, 1, 7, 9, 5, 8, 4, 2]
[4, 9, 5, 1, 3, 6, 7, 2, 8]
[7, 8, 6, 5, 2, 4, 1, 9, 3]
[1, 3, 2, 8, 7, 9, 4, 6, 5]
[6, 1, 3, 4, 8, 2, 5, 7, 9]
[9, 5, 4, 3, 6, 7, 2, 8, 1]
[8, 2, 7, 9, 5, 1, 6, 3, 4]


Input:
{input}

Output:
'''

cot_prompt = '''

'''

value_prompt = '''Evaluate whether a selected empty Sudoku cell has a valid value based on Sudoku constraints (sure/maybe/impossible).

Rules:
- Each row must contain digits 1-9 without repetition.
- Each column must contain digits 1-9 without repetition.
- Each 3x3 box must contain digits 1-9 without repetition.
- sure = exactly one valid digit can go in the selected cell.
- maybe = more than one valid digit can go in the selected cell.
- impossible = no digit can go in the selected cell.

Input:
Board:
[5, 3, 0, 0, 7, 0, 0, 0, 0]
[6, 0, 0, 1, 9, 5, 0, 0, 0]
[0, 9, 8, 0, 0, 0, 0, 6, 0]
[8, 0, 0, 0, 6, 0, 0, 0, 3]
[4, 0, 0, 8, 0, 3, 0, 0, 1]
[7, 0, 0, 0, 2, 0, 0, 0, 6]
[0, 6, 0, 0, 0, 0, 2, 8, 0]
[0, 0, 0, 4, 1, 9, 0, 0, 5]
[0, 0, 0, 0, 8, 0, 0, 7, 9]

Selected cell: r1c3
Valid values for r1c3 are 1, 2, and 4.
maybe

Input:
Board:
[5, 3, 4, 6, 7, 8, 9, 1, 0]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]

Selected cell: r1c9
Only digit 2 can go in r1c9.
sure

Input:
Board:
[5, 3, 0, 0, 7, 0, 0, 0, 0]
[6, 0, 0, 1, 9, 5, 0, 0, 0]
[0, 9, 8, 0, 0, 0, 0, 6, 0]
[8, 0, 0, 0, 6, 0, 0, 0, 3]
[4, 0, 0, 8, 0, 3, 0, 0, 1]
[7, 0, 0, 0, 2, 0, 0, 0, 6]
[0, 6, 0, 0, 0, 0, 2, 8, 0]
[0, 0, 0, 4, 1, 9, 0, 0, 5]
[0, 0, 0, 0, 8, 0, 0, 7, 9]
Selected cell: r1c3
Proposed digit: 5

Digit 5 already exists in row 1, so it cannot go in r1c3.
impossible

Input:
{input}
'''

propose_prompt = '''Let's play a 9x9 sudoku puzzle, where each 0 entry corresponds to an empty square that must be filled.

{input}

Given the current status, list all possible answers for unfilled or changed squares, and your confidence levels (certain/high/medium/low), using the format "r1c4. 7 (medium)". Use "certain" cautiously and only when you are 100% sure this is the correct number. You can list more then one possible answer for each element.
'''
