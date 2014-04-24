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


cells = []


class MainLayout(FloatLayout):
    cell_grid = ObjectProperty()
    command_grid = ObjectProperty()
    voloda = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.task = Task(1)

    def make(self):
        delta = 0.1
        for x in range(self.task.axis_x):
            cells.append([])
            for y in range(self.task.axis_y):
                cell = Cell(pos_hint={'x': x * 0.1 + delta, 'y': y * 0.1 + delta})
                cells[x].append(cell)
                self.cell_grid.add_widget(cell)
        self.voloda = Voloda(cell_x=self.task.start_x, cell_y=self.task.start_y)
        for coord in self.task.drops_coords:
            self.cell_grid.add_widget(GoalDrop(pos_hint=cells[coord['x']][coord['y']].pos_hint))
        self.cell_grid.add_widget(StartPoint(pos_hint=cells[self.task.start_x][self.task.start_y].pos_hint))

    def open_command_popup(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='hello', on_press=self.define_button))
        popup = Popup(title='Commands', content=box)
        popup.size_hint = (0.2, 0.8)
        popup.open()

    def run(self):
        self.cell_grid.remove_widget(self.voloda)
        self.voloda.cell_x = self.task.start_x
        self.voloda.cell_y = self.task.start_y
        self.voloda.pos = cells[self.voloda.cell_x][self.voloda.cell_y].pos
        self.cell_grid.add_widget(self.voloda)
        animator = Animator()
        for command in global_command_stuff.commands:
            animator.add_animation({'animation': command.do(self.voloda, cells), 'widget': self.voloda})
        animator.play()

    def define_button(self, *args):
        index = len(global_command_stuff.commands) + 1
        command = CommandTurn(index)
        global_command_stuff.commands.append(command)
        command_widget = command.build_widget()
        self.command_grid.add_widget(command_widget)


class Cell(Widget):
    pass


class Voloda(Widget):
    def __init__(self, **kwargs):
        super(Voloda, self).__init__(**kwargs)
        self.cell_x = kwargs['cell_x']
        self.cell_y = kwargs['cell_y']
        self.face_to = 'north'


class GoalDrop(Widget):
    def __init__(self, **kwargs):
        super(GoalDrop, self).__init__(**kwargs)


class StartPoint(Widget):
    def __init__(self, **kwargs):
        super(StartPoint, self).__init__(**kwargs)