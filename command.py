__author__ = 'arthurnum'


from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty



class CommandLineWidget(Widget):
    id_command_label = ObjectProperty()
    text_command_label = ObjectProperty()
    delete_button = ObjectProperty()
    command_link = ObjectProperty()

    def __init__(self, command, **kwargs):
        super(CommandLineWidget, self).__init__(**kwargs)
        self.id_command_label.text = "%d." % command.cid
        self.text_command_label.text = command.text
        self.command_link = command


class Command:
    cid = NumericProperty(0)
    text = StringProperty('')


class CommandMove(Command):
    def __init__(self, cid):
        self.cid = cid
        self.text = 'move'

    def do(self, voloda, cells):
        voloda.cell_x += 1
        dest_cell = cells[voloda.cell_x][voloda.cell_y]
        anim = Animation(x=dest_cell.x, y=dest_cell.y, duration=0.5)
        anim.start(voloda)


class CommandWait:

    def do(self):
        pass


