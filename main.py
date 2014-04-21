__author__ = 'arthurnum'


from kivy.app import App
from kivy.lang import Builder
from main_layout import MainLayout
from kivy.core.window import Window

Builder.load_file('main.kv')

# 1920x1200
class MyApp(App):

    def build(self):
        # Window.size = (960, 600)
        layout = MainLayout()
        layout.make()
        return layout


MyApp().run()

