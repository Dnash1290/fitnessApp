from main5 import ForgotPassword
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.button import Button

from kivy.uix.modalview import ModalView
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App

Builder.load_file("kivy_gui/menu.kv")



class Menu(Screen):
    def on_press(sedfg):
        print("dsjlfvolcs")
        pass 

class MyApp(App):
    def build(self):
        return Menu()

if __name__ =="__main__":
    MyApp().run()
