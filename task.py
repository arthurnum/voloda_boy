__author__ = 'arthurnum'


import yaml
from animator import Animator
from graphics import *


class Task():
    def __init__(self, task_number):
        file_name = "tasks/task%d.yaml" % task_number
        stream = open(file_name, 'r')
        data = yaml.load(stream)
        stream.close()
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
                    Animator().schedule_drop_score_animation(goal_drop, self.drops_board)