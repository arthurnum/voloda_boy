__author__ = 'arthurnum'


from kivy.app import App
from kivy.lang import Builder
from main_layout import MainLayout
from kivy.core.window import Window
from command_stuff import global_command_stuff

Builder.load_file('main.kv')


# 1920x1200
class MyApp(App):

    def build(self):
        Window.size = (960, 600)
        layout = MainLayout()
        layout.make()
        global_command_stuff.link_to_command_grid = layout.command_grid
        return layout


MyApp().run()
