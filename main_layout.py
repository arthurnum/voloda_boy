__author__ = 'arthurnum'


from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from functools import partial
from command import CommandTurn
from command import CommandLineWidget
from kivy.uix.label import Label
from kivy.animation import Animation
from command_stuff import global_command_stuff
from task import Task
from animator import Animator


class MainLayout(FloatLayout):
    cell_grid = ObjectProperty()
    command_grid = ObjectProperty()
    voloda = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.task = Task(1)
        self.locked = False

    # http://stackoverflow.com/questions/7590682/access-self-from-decorator
    def lock(func):
        def _decorator(self, *args, **kwargs):
            if not self.locked:
                func(self, *args, **kwargs)
        return _decorator

    def make(self):
        for row in self.task.cells:
            for cell in row:
                self.cell_grid.add_widget(cell)
        for drop_score in self.task.drops_board.drops:
            self.cell_grid.add_widget(drop_score)
        self.voloda = self.task.get_voloda()
        for goal_drop in self.task.get_goal_drops():
            self.drop = goal_drop
            self.cell_grid.add_widget(goal_drop)
        self.cell_grid.add_widget(self.task.get_start_point())

    @lock
    def open_command_popup(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='hello', on_press=self.define_button))
        popup = Popup(title='Commands', content=box)
        popup.size_hint = (0.2, 0.8)
        popup.open()

    @lock
    def run(self):
        self.locked = True
        self.reset_voloda()
        Animator().play(global_command_stuff.commands, self.task, self.voloda, self.after_play)

    def define_button(self, *args):
        index = len(global_command_stuff.commands) + 1
        command = CommandTurn(index)
        global_command_stuff.commands.append(command)
        command_widget = command.build_widget()
        self.command_grid.add_widget(command_widget)

    def reset_voloda(self):
        self.voloda.cell_x = self.task.start_x
        self.voloda.cell_y = self.task.start_y
        self.voloda.pos = self.task.cells[self.voloda.cell_x][self.voloda.cell_y].pos
        self.cell_grid.add_widget(self.voloda)

    def after_play(self, *args):
        if self.task.drops_board.filled == self.task.drops_count:
            pass
        else:
            self.cell_grid.remove_widget(self.voloda)
            self.task.reset_goal_drops()
            self.locked = False
