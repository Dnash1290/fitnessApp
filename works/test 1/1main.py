from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField

class MyImage(Screen):
    pass
class MyApp(MDApp):
    def build(self):
        return MyImage()


MyApp().run()
