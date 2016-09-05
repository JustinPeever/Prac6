from kivy.app import App
from kivy.lang import Builder


class ConvertApp(App):
    def build(self):
        self.title = "Convert Miles to Kilo Metres"
        self.root = Builder.load_file('Convert.kv')
        return self.root

ConvertApp().run()