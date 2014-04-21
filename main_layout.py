__author__ = 'arthurnum'


from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from functools import partial
from command import CommandMove
from command import CommandLineWidget
from kivy.uix.label import Label
from kivy.animation import Animation


cells = []
commands = []


class MainLayout(FloatLayout):
    cell_grid = ObjectProperty()
    command_grid = ObjectProperty()
    voloda = ObjectProperty()

    def make(self):
        delta = 0.1
        for x in range(5):
            cells.append([])
            for y in range(5):
                cell = Cell(pos_hint={'x': x * 0.1 + delta, 'y': y * 0.1 + delta})
                cells[x].append(cell)
                self.cell_grid.add_widget(cell)
        self.voloda = Voloda()
        # self.cell_grid.add_widget(self.voloda)

    def open_command_popup(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='hello', on_press=self.define_button))
        popup = Popup(title='Commands', content=box)
        popup.size_hint = (0.2, 0.8)
        popup.open()

    def run(self):
        anim = Animation(duration=0.0)
        for command in commands:
            anim += command.do(self.voloda, cells)
        anim.start(self.voloda)

    def define_button(self, *args):
        index = len(commands) + 1
        command = CommandMove(index)
        commands.append(command)
        command_widget = command.build_widget()
        self.command_grid.add_widget(command_widget)

    def delete_command(self, command, *args):
        self.command_grid.remove_widget(command.command_widget)
        commands.remove(command)
        i = 1
        for command in commands:
            command.cid = i
            command.update_widget()
            i += 1


class Cell(Widget):
    pass


class Voloda(Widget):
    def __init__(self, **kwargs):
        super(Voloda, self).__init__(**kwargs)
        self.cell_x = 0
        self.cell_y = 0
        self.face_to = 'north'
