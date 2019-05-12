#kivy.require("1.10.1")su
from kivy.app import App, StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
from kivy.properties import BooleanProperty

from calc import calc


class CalcWindow(App, BoxLayout):
    the_text = StringProperty()
    nawiasy = BooleanProperty(False)

    def wynik(self, text):
        if text == "None":
            return ""
        elif text[0:4] == "None":
            return str(calc(text[4:]))
        return str(calc(text))

    def lewyNawias(self, text):
        CalcWindow.nawiasy = True
        if text == "" or text[-1].isnumeric() is False:
            return "("
        else:
            return "*("

    def prawyNawias(self, text):
        if CalcWindow.nawiasy is True:
            if text[-1] is not "(":
                CalcWindow.nawiasy = False
                return ")"
        else:
            return ""


    def build(self):
        Builder.load_file('calc.kv')
        return CalcWindow()

if __name__ == "__main__":
    CalcWindow().run()