__author__ = 'arthurnum'


from kivy.clock import Clock
from functools import partial


class Animator:
    def __init__(self):
        self.animations = []

    def add_animation(self, animation):
        self.animations.append(animation)

    def play(self):
        delay = 0.0
        for animation in self.animations:
            Clock.schedule_once(partial(self.schedule_animation, animation['animation'], animation['widget']), delay)
            delay += 0.5

    def schedule_animation(self, animation, widget, *args):
        animation.start(widget)