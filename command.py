__author__ = 'arthurnum'


from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.modalview import ModalView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from functools import partial
from command_stuff import global_command_stuff



class CommandLineWidget(Widget):
    id_command_label = ObjectProperty()
    text_command_label = ObjectProperty()

    def __init__(self, command, **kwargs):
        super(CommandLineWidget, self).__init__(**kwargs)
        self.id_command_label.text = "%d." % command.cid
        self.text_command_label.text = command.text
        self.command = command

    def update(self, command):
        self.id_command_label.text = "%d." % command.cid
        if command.arg is not None:
            self.text_command_label.text = "%s %s" % (command.text, str(command.arg))
        else:
            self.text_command_label.text = command.text

    def on_touch_down(self, touch):
        self.canvas.before.clear()
        if self.collide_point(touch.x, touch.y):
            with self.canvas.before:
                Color(0.5, 0.6, 0.7, 0.33)
                Rectangle(pos=self.pos, size=self.size)
            popup = CommandEditWidget(self.command)
            popup.open()
        else:
            with self.canvas.before:
                Color(1, 1, 1, 0)
                Rectangle(pos=self.pos, size=self.size)
        for child in self.children:
            child.on_touch_down(touch)


class CommandEditWidget(ModalView):
    def __init__(self, command, **kwargs):
        super(CommandEditWidget, self).__init__(**kwargs)
        self.background_color = [0, 0, 0, .33]
        self.background = 'images/modal_view.png'
        self.border = [0, 0, 0, 0]
        self.size_hint = (0.66, 0.5)
        layout = StackLayout(spacing=1)
        title = "%d. %s" % (command.cid, command.text)
        layout.add_widget(Label(text=title, size_hint=[1.0, 0.1]))
        layout.add_widget(Label(text='Argument:', size_hint=[0.3, 0.12]))
        self.arg_text_input = TextInput(text=str(command.arg), multiline=False, size_hint=[0.5, 0.12])
        layout.add_widget(self.arg_text_input)
        arg_box = BoxLayout(orientation='horizontal', spacing=1, size_hint=[1.0, 0.2])
        for arg in command.get_available_args():
            arg_box.add_widget(Button(text=str(arg), on_press=partial(self.set_argument, command, arg)))
        layout.add_widget(arg_box)
        layout.add_widget(Button(text='None', size_hint=[1.0, 0.2], on_press=partial(self.set_argument, command, None)))
        delete_box = FloatLayout(size_hint=[1.0, 0.3])
        delete_box.add_widget(Button(text='DELETE', size_hint=[0.3, 0.4], pos_hint={'x': 0.6, 'y': 0.0}, on_press=partial(self.delete_command, command)))
        layout.add_widget(delete_box)
        self.add_widget(layout)

    def set_argument(self, command, arg, *args):
        command.arg = arg
        self.arg_text_input.text = str(arg)
        command.update_widget()

    def delete_command(self, command, *args):
        global_command_stuff.delete_command(command)
        self.dismiss()


class Command:
    cid = NumericProperty(0)
    text = StringProperty('')
    command_widget = ObjectProperty()

    def build_widget(self):
        self.command_widget = CommandLineWidget(self)
        return self.command_widget

    def update_widget(self):
        self.command_widget.update(self)


class CommandMove(Command):
    def __init__(self, cid, arg=None):
        self.cid = cid
        self.text = 'move'
        self.arg = arg

    def do(self, voloda, cells):
        dest = self.arg
        if dest not in self.get_available_args():
            dest = voloda.face_to

        dest_cell = cells[voloda.cell_x][voloda.cell_y]

        if dest == 'north':
            voloda.cell_y += 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]
        elif dest == 'south':
            voloda.cell_y -= 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]
        elif dest == 'west':
            voloda.cell_x -= 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]
        elif dest == 'east':
            voloda.cell_x += 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]

        voloda.face_to = dest
        anim = Animation(x=dest_cell.x, y=dest_cell.y, duration=0.5)
        return anim

    def get_available_args(self):
        return ['north', 'south', 'west', 'east']


class CommandWait:

    def do(self):
        pass


