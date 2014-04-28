__author__ = 'arthurnum'


from kivy.uix.widget import Widget


class Cell(Widget):
    pass


class GoalDrop(Widget):
    def __init__(self, **kwargs):
        super(GoalDrop, self).__init__(**kwargs)


class StartPoint(Widget):
    def __init__(self, **kwargs):
        super(StartPoint, self).__init__(**kwargs)


class Voloda(Widget):
    def __init__(self, **kwargs):
        super(Voloda, self).__init__(**kwargs)
        self.cell_x = kwargs['cell_x']
        self.cell_y = kwargs['cell_y']
        self.face_to = 'north'