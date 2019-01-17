import kivy
kivy.require ("1.10.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from math import sqrt,pow,pi

class calculayout(GridLayout):
    def calculate(self,ex):
        if ex:
            try:
                self.dis.text = str(eval(ex))
            except:
                self.dis.text="math error"
        else:
            pass



class calculatorApp(App):
    def build(self):
        return calculayout()

if __name__=="__main__":
    calculatorApp().run()