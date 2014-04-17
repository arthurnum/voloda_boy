__author__ = 'arthurnum'


from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from functools import partial
from command import CommandMove
from command import CommandLineWidget
from kivy.uix.label import Label


cells = []
commands = []


class MainLayout(BoxLayout):
    cell_grid = ObjectProperty()
    command_grid = ObjectProperty()
    voloda = ObjectProperty()

    def make(self):
        for x in range(5):
            cells.append([])
            for y in range(5):
                cell = Cell(pos_hint={'x': x * 0.2, 'y': y * 0.2})
                cells[x].append(cell)
                self.cell_grid.add_widget(cell)
        self.voloda = Voloda()
        self.cell_grid.add_widget(self.voloda)

    def open_command_popup(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='hello', on_press=self.define_button))
        box.add_widget(Button(text='hello', on_press=self.define_button))
        box.add_widget(Button(text='hello', on_press=self.define_button))
        box.add_widget(Button(text='hello', on_press=self.define_button))
        box.add_widget(Button(text='hello', on_press=self.define_button))
        box.add_widget(Button(text='hello', on_press=self.define_button))
        box.add_widget(Button(text='hello', on_press=self.define_button))
        box.add_widget(Button(text='hello', on_press=self.define_button))
        popup = Popup(title='Commands', content=box)
        popup.size_hint = (0.2, 0.8)
        popup.open()

    def run(self):
        for command in commands:
            command.do(self.voloda, cells)

    def define_button(self, *args):
        command = CommandMove(len(commands) + 1)
        commands.append(command)
        command_widget = CommandLineWidget(command)
        command_widget.delete_button.bind(on_press=partial(self.delete_command, command_widget))
        self.command_grid.add_widget(command_widget)


    def delete_command(self, command_widget, *args):
        commands.remove(command_widget.command_link)
        self.command_grid.remove_widget(command_widget)
        command_widget = None


class Cell(Widget):
    pass


class Voloda(Widget):
    def __init__(self, **kwargs):
        super(Voloda, self).__init__(**kwargs)
        self.cell_x = 0
        self.cell_y = 0
