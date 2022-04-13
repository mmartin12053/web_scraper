import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class dave(GridLayout):
    def pressed(self, text):
        f = open("main.txt", "a")
        f.write(f"{text}\n")
        f.close()

class myApp(App):
     pass



if __name__ == '__main__':
     myApp().run()




