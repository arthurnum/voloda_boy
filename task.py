__author__ = 'arthurnum'


import yaml
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
        drops = []
        for coord in self.drops_coords:
            drops.append(GoalDrop(pos_hint=self.cells[coord['x']][coord['y']].pos_hint))
        return drops

    def get_start_point(self):
        return StartPoint(pos_hint=self.cells[self.start_x][self.start_y].pos_hint)