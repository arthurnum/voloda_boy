__author__ = 'arthurnum'


from kivy.uix.widget import Widget
from kivy.properties import NumericProperty


class Cell(Widget):
    pass


class GoalDrop(Widget):
    def __init__(self, x, y, **kwargs):
        super(GoalDrop, self).__init__(**kwargs)
        self.free = True
        self.cell_x = x
        self.cell_y = y



class StartPoint(Widget):
    def __init__(self, **kwargs):
        super(StartPoint, self).__init__(**kwargs)


class Voloda(Widget):
    cell_x = NumericProperty(0)
    cell_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Voloda, self).__init__(**kwargs)
        self.cell_x = kwargs['cell_x']
        self.cell_y = kwargs['cell_y']
        self.face_to = 'north'


class DropScore(Widget):
    def __init__(self, **kwargs):
        super(DropScore, self).__init__(**kwargs)


class DropScoreBoard:
    def __init__(self, count):
        self.filled = 0
        delta = 0.1
        self.drops = []
        for x in range(count):
            self.drops.append(DropScore(pos_hint={'x': x * 0.06 + delta, 'y': 0.02}))
