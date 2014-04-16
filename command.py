__author__ = 'arthurnum'


from kivy.animation import Animation


class Command:
    pass


class CommandMove:

    def do(self, voloda, cells):
        voloda.cell_x += 1
        dest_cell = cells[voloda.cell_x][voloda.cell_y]
        anim = Animation(x=dest_cell.x, y=dest_cell.y, duration=0.5)
        anim.start(voloda)


class CommandWait:

    def do(self):
        pass


