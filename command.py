__author__ = 'arthurnum'


from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.graphics import Color, Rectangle



class CommandLineWidget(Widget):
    id_command_label = ObjectProperty()
    text_command_label = ObjectProperty()
    delete_button = ObjectProperty()
    command_link = ObjectProperty()

    def __init__(self, command, **kwargs):
        super(CommandLineWidget, self).__init__(**kwargs)
        self.id_command_label.text = "%d." % command.cid
        self.text_command_label.text = command.text

    def update(self, command):
        self.id_command_label.text = "%d." % command.cid

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            with self.canvas.before:
                Color(0.5, 0.6, 0.7)
                Rectangle(pos=self.pos, size=self.size)
        else:
            with self.canvas.before:
                Color(0.4, 0.5, 0.7)
                Rectangle(pos=self.pos, size=self.size)
        for child in self.children:
            child.on_touch_down(touch)



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
        # anim.start(voloda)


class CommandWait:

    def do(self):
        pass


