__author__ = 'arthurnum'


from animator import Animator
from graphics import *


LEVELS = [
    {
        'axis_x': 1,
        'axis_y': 5,
        'start': {
            'x': 0,
            'y': 0
        },
        'drops': {
            'count': 4,
            'coords': [{'x': 0, 'y': 2}, {'x': 0, 'y': 1}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4}]
        }
    },
    {
        'axis_x': 2,
        'axis_y': 5,
        'start': {
            'x': 1,
            'y': 1
        },
        'drops': {
            'count': 2,
            'coords': [{'x': 0, 'y': 2}, {'x': 1, 'y': 3}]
        }
    },
]


class Task():
    def __init__(self, task_number):
        data = LEVELS[task_number]
        self.axis_x = data['axis_x']
        self.axis_y = data['axis_y']
        self.start_x = data['start']['x']
        self.start_y = data['start']['y']
        self.drops_count = data['drops']['count']
        self.drops_coords = data['drops']['coords']
        self.cells = self.init_cells()
        self.drops_board = DropScoreBoard(data['drops']['count'])
        self.goal_drops = None

    def init_cells(self):
        delta = 0.1
        cells = []
        for x in range(self.axis_x):
            cells.append([])
            for y in range(self.axis_y):
                cell = Cell(pos_hint={'x': x * 0.1 + delta, 'y': y * 0.1 + delta})
                cells[x].append(cell)
        return cells

    def get_voloda(self):
        return Voloda(cell_x=self.start_x, cell_y=self.start_y)

    def get_goal_drops(self):
        if not self.goal_drops:
            self.goal_drops = []
            for coord in self.drops_coords:
                self.goal_drops.append(GoalDrop(coord['x'], coord['y'], pos_hint=self.cells[coord['x']][coord['y']].pos_hint))
        return self.goal_drops

    def get_start_point(self):
        return StartPoint(pos_hint=self.cells[self.start_x][self.start_y].pos_hint)

    def check_drops_collide(self, voloda):
        for goal_drop in self.goal_drops:
            if goal_drop.free:
                if (voloda.cell_x == goal_drop.cell_x) and (voloda.cell_y == goal_drop.cell_y):
                    goal_drop.free = False
                    Animator().schedule_drop_score_animation(goal_drop, self.drops_board)

    def reset_goal_drops(self):
        self.drops_board.filled = 0
        for goal_drop in self.goal_drops:
            if not goal_drop.free:
                goal_drop.free = True
                goal_drop.size_hint = (0.1, 0.1)
                goal_drop.pos = self.cells[goal_drop.cell_x][goal_drop.cell_y].pos