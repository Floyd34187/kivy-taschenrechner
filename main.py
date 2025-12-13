import kivy
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')

    
class MyBoxLayout(BoxLayout):
    def rechne(self,operation):
        try:
            z1 = float(self.ids.tfZ1.text)
            z2 = float(self.ids.tfZ2.text)
            erg = 0.0
            if operation=="+":
                erg = z1+z2
            elif operation=="-":
                erg = z1-z2
            elif operation=="*":
                erg = z1*z2
            elif operation=="/":
                erg = z1/z2
            self.ids.tfErg.text = str(erg)
        except:
            self.ids.tfErg.text = "undefined operation"


class TaschenrechnerApp(App):
    def build(self):
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    TaschenrechnerApp().run()


