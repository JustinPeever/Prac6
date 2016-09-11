

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty



class list(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.List = {"B B": "04", "C C": "11", "O O": "456"}

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "littlelist"
        self.root = Builder.load_file('littlelist.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.List:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.List[name])

    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        self.root.ids.entriesBox.clear_widgets()

list().run()
