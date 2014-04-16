__author__ = 'arthurnum'


from kivy.app import App
from kivy.lang import Builder
from main_layout import MainLayout

Builder.load_file('main.kv')


class MyApp(App):

    def build(self):
        layout = MainLayout()
        layout.make()
        return layout


MyApp().run()

