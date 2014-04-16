__author__ = 'arthurnum'


from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class CommandLineWidget(Widget):
    def __init__(self, **kwargs):
        super(CommandLineWidget, self).__init__(**kwargs)
        id_lane_label = Label(text='1.', size_hint=[0.2, 1.0])
        self.add_widget(id_lane_label)


class CommandMove:

    def do(self, voloda, cells):
        voloda.cell_x += 1
        dest_cell = cells[voloda.cell_x][voloda.cell_y]
        anim = Animation(x=dest_cell.x, y=dest_cell.y, duration=0.5)
        anim.start(voloda)


class CommandWait:

    def do(self):
        pass


