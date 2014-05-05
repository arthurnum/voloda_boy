__author__ = 'arthurnum'


from kivy.clock import Clock
from functools import partial
from kivy.animation import Animation


class Animator:

    def play(self, commands, task, voloda, after_play_callback):
        delay = 0.0
        for command in commands:
            Clock.schedule_once(partial(self.schedule_voloda_animation, command, task, voloda), delay)
            delay += 0.5
        Clock.schedule_once(after_play_callback, delay + 1.5)

    def schedule_voloda_animation(self, command, task, voloda, *args):
        command.do(voloda, task.cells).start(voloda)
        task.check_drops_collide(voloda)

    def schedule_drop_score_animation(self, goal_drop, board, *args):
        goal_drop.pos_hint = {}
        dest = board.drops[board.filled]
        board.filled += 1
        anim = Animation(pos=dest.pos, t='in_out_back')
        anim &= Animation(size_hint=(0.06, 0.06))
        anim.start(goal_drop)