__author__ = 'arthurnum'


from kivy.uix.widget import Widget
from kivy.properties import NumericProperty


class Cell(Widget):
    pass


class GoalDrop(Widget):
    def __init__(self, **kwargs):
        super(GoalDrop, self).__init__(**kwargs)


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

    def on_cell_x(self, instance, value):
        self.check_position(value)

    def on_cell_y(self, instance, value):
        self.check_position(value)

    def check_position(self, value):
        pass