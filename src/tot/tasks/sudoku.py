import re
import os
import json
from tot.tasks.base import Task, DATA_PATH
from tot.prompts.sudokus import * 
from tot.models import gpt

# work on this later
class SudokuEnv:
    def __init__(self, file='sudoku_9.json'):
        self.file = os.path.join(DATA_PATH, 'crosswords', file)

        self.file = json.load(open(self.file))
        self.n = len(self.file)
        self.cache = {}
        self.idx = None
        self.times = 0
        self.prompt_status_cache = {}


    def __len__(self):
        return self.n

    def reset(self, idx, board = None, status = None, steps = None):
        self.idx = idx
        self.data, self.board_get = self.file[idx]

        self.board = [row[:] for row in self.data]
        self.board_gt = [row[:] for row in self.board]

        self.steps = 0

        self.status = [[0 for _ in range(9)] for _ in range(9)]

        if board is not None:
            self.board = [row[:] for row in board]
        
        if status is not None:
            self.staus = status
        
        if steps is not None:
            self.steps = steps

        return self.render()
    
    # this one is tricky
    # how to change for sudoku
    def prompt_status(self):
        count = {'sure': 0, 'maybe': 0, 'impossible': 0}
        for ans, data, status in zip(self.ans, self.data, self.status):
            # if status != 0: continue
            if ans.count('_') >= 4: continue
            ans = ' '.join(ans.lower())
            line = f'{data}: {ans}'
            prompt = value_prompt.format(input=line) #where is value_prompt
            if prompt in self.prompt_status_cache:
                res = self.prompt_status_cache[prompt]
            else:
                res = gpt(prompt)[0]
                self.prompt_status_cache[prompt] = res

            res = res.split('\n')[-1].strip()
            if res in count: count[res] += 1

        return count
    
    def render_gt_board(self):
        s = "GT Board:\n"
        for i in range(9):
            s += ' '.join(self.board_gt[i*9:(i+1)*9]) + '\n'
        return s

    def render_board(self):
        s = "Current Board:\n"
        for i in range(9):
            s += ''.join(self.board[i*9:(i+1)*9]) + '\n'
        return s
    
    # predicted answer
    def render_ans(self, status=None):
        s = ""

        for i in range(9):
            row = []
            for j in range(9):
                if status is None or self.status[i][j] == status:
                    row.append(str(self.ans[i][j]))
                else:
                    row.append(str(self.data[i][j]))

            s += " ".join(row) + "\n"

        return s
    
    # actual answer
    def render_gt_ans(self, status=None):
        s = ""

        for i in range(9):
            row = []
            for j in range(9):
                if status is None or self.status[i][j] == status:
                    row.append(str(self.ans_gt[i][j]))
                else:
                    row.append(str(self.data[i][j]))

            s += " ".join(row) + "\n"

        return s
    
    def render(self, status=True):
        if status:
            return (
                self.render_board()
                + '\nUnfilled:\n'
                + self.render_ans(status=0)
                + '\nFilled:\n'
                + self.render_ans(status=1)
            )
        else:
            return self.render_board() + '\n' + self.render_ans()
        
    def get_ans(self, board):
        ans = []

        # rows
        for i in range(9):
            ans.append(''.join(str(x) for x in board[i]))

        # columns
        for j in range(9):
            ans.append(''.join(str(board[i][j]) for i in range(9)))

        return ans

    def step(self, action):
        self.steps += 1

        action = action.split('\n')[-1]
        action = action.split('. ')

        if len(action) != 2:
            return 'Invalid! Format should be like "r1c3. 5"', 0, False, {}

        pos, value = action

        if len(pos) != 4 or pos[0] != 'r' or pos[2] != 'c':
            return 'Invalid! Position should be like r1c1 to r9c9', 0, False, {}

        try:
            row = int(pos[1]) - 1
            col = int(pos[3]) - 1
            value = int(value)
        except:
            return 'Invalid! Row, column, and value must be numbers.', 0, False, {}

        if row < 0 or row >= 9 or col < 0 or col >= 9:
            return 'Invalid! Row and column must be between 1 and 9.', 0, False, {}

        if value < 1 or value > 9:
            return 'Invalid! Value must be between 1 and 9.', 0, False, {}

        if self.data[row][col] != 0:
            return 'Invalid! This cell is already filled.', 0, False, {}

        self.board[row][col] = value

        self.new_ans = self.get_ans(self.board)

        self.status = [
            [
                2 if self.board[i][j] != self.board_gt[i][j] and self.board[i][j] != 0
                else self.status[i][j]
                for j in range(9)
            ]
            for i in range(9)
        ]

        self.status[row][col] = 1
        self.ans = self.new_ans

        r_all = self.board == self.board_gt

        correct = 0
        total_filled = 0

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    total_filled += 1
                    if self.board[i][j] == self.board_gt[i][j]:
                        correct += 1

        r_cell = correct / 81
        r_filled = correct / total_filled if total_filled > 0 else 0

        return self.render(), r_all, (r_all or self.steps >= 81), {
            'r_cell': r_cell,
            'r_filled': r_filled,
            'r_game': r_all
        }


class SudokuTask:
    '''
        def __init__(self, file='mini0505.json'):
        """
        file: a csv file (fixed)
        """
        super().__init__()
        self.env = MiniCrosswordsEnv(file)  # use it as a stateless tool
        self.xs = []
        for idx in range(len(self.env)):
            self.env.reset(idx)
            self.xs.append(self.env.render_clues())
        self.steps = 10  
        to-do : variable steps??
        self.cache_proposals = {}
    '''

        # Input (x): Desc of 9x9 sudoku puzzle
        # Output (x) : Completed Sudoku Grid
        # Reward (r) : cell-level and puzzle-level
    def __init__(self, file = 'sudoku_9.json'):
        super().__init__()

        self.env = SudokuEnv(file)      # set up the environment
        self.xs = []

        for idx in range(len(self.env)):
            self.env.reset(idx)
            self.xs.append(self.env.render_board())

        # 9 x 9 board instead of 5 x 5
        self.steps = 81
        self.cache_proposals = {}

    def __len__(self) -> int:
        return len(self.env)

    def get_input(self, idx: int) -> str:
        self.env.reset(idx)

        return self.env.render_board()

    def test_output(self, idx: int, output: str):
        self.env.reset(idx)
        output = output.split('Output:\n')[-1].strip()

        lines = output.split('\n')[-9:]
        board = []

        for line in lines:
            nums = [int(x) for x in line.strip().split()[:-9]]
            board.append(nums)

        info = self.env.evaluate_board(board)
        info['r'] = info['r_cell']

        return info
    
    def set_status(self, x: str, y: str):
        idx = self.xs.index(x.strip())

        self.test_output(idx, y)

    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y
        # go back and fix this for the data input file
        #standard_prompt should be the variable of the text input

    # possibly remove this
    @staticmethod
    def cot_prompt_wrap(x: str, y: str = '') -> str:
        return cot_prompt.format(input = x) + y
        # again same thing here

    def propose_prompt_wrap():
        pass

    def propose_outputs_unwrap(self, x: str, y: str, outputs: list, n_max_propose: int) -> list:
        confidence_to_value = {
            'certain': 1,
            'high': 0.5,
            'medium': 0.2,
            'low': 0.1
        }

        proposals_to_scores = {}

        for output in outputs:
            lines = output.split('\n')

            # Example expected line: r1c3. 5 (high)
            pattern = r'^(r[1-9]c[1-9])\. ([1-9]) \((certain|high|medium|low)\).*$'

            for line in lines:
                match = re.match(pattern, line.strip())

                if match:
                    pos = match.group(1).lower()
                    value = match.group(2)
                    confidence = match.group(3)

                    proposal = pos + '. ' + value
                    score = confidence_to_value.get(confidence, 0)

                    proposals_to_scores[proposal] = proposals_to_scores.get(proposal, 0) + score

        proposals = sorted(
            proposals_to_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        if n_max_propose != -1:
            proposals = proposals[:n_max_propose]

        proposals = [y + proposal[0] + '\n' for proposal in proposals]

        self.cache_proposals[(x, y, n_max_propose)] = proposals

        return proposals

    # change this one also
    def evaluate(self, x: str, y: str, n_evaluate_sample: int) -> int:
        self.set_status(x, y)
        assert n_evaluate_sample == 1 # TODO: ad hoc
        count = {'sure': 0, 'maybe': 0, 'impossible': 0}
        for ans, data, status in zip(self.env.ans, self.env.data, self.env.status):
            if ans.count('_') >= 4: continue
            ans = ' '.join(ans.lower())
            line = f'{data}: {ans}'
            prompt = value_prompt.format(input=line)
            res = gpt(prompt)[0]
            print(line)
            print(res)
            print()
            res = res.split('\n')[-1].strip()
            if res in count: count[res] += 1
        print(count)
        return count
