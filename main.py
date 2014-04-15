from kivy.core.window import WindowBase

__author__ = 'arthurnum'


from kivy.uix.behaviors import DragBehavior
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
import kivy.core.window
from kivy.properties import BooleanProperty
from main_layout import MainLayout

Builder.load_file('main.kv')





class MyApp(App):

    def build(self):
        return MainLayout()


MyApp().run()

