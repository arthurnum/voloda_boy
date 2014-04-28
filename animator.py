__author__ = 'arthurnum'


from kivy.clock import Clock
from functools import partial


class Animator:

    def play(self, commands, task, voloda):
        delay = 0.0
        for command in commands:
            Clock.schedule_once(partial(self.schedule_animation, command, task, voloda), delay)
            delay += 0.5

    def schedule_animation(self, command, task, voloda, *args):
        command.do(voloda, task.cells).start(voloda)