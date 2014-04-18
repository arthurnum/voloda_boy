__author__ = 'arthurnum'


from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.modalview import ModalView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button



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
        title = "%d. %s" % (command.cid, command.text)
        self.size_hint = (0.5, 0.5)
        layout = StackLayout()
        layout.add_widget(Label(text=title, size_hint=[None, None]))
        layout.add_widget(Label(text='Sho za huita', size_hint=[None, None]))
        # create a dropdown with 10 buttons
        dropdown = DropDown()
        for index in range(10):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=22)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        layout.add_widget(mainbutton)

        self.add_widget(layout)


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
        if self.arg not in ['north', 'south', 'west', 'east']:
            self.arg = voloda.face_to

        dest_cell = cells[voloda.cell_x][voloda.cell_y]

        if self.arg == 'north':
            voloda.cell_y += 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]
        elif self.arg == 'south':
            voloda.cell_y -= 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]
        elif self.arg == 'west':
            voloda.cell_x -= 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]
        elif self.arg == 'east':
            voloda.cell_x += 1
            dest_cell = cells[voloda.cell_x][voloda.cell_y]

        voloda.face_to = self.arg
        anim = Animation(x=dest_cell.x, y=dest_cell.y, duration=0.5)
        return anim

    def get_available_args(self):
        return ['north', 'south', 'west', 'east']


class CommandWait:

    def do(self):
        pass


