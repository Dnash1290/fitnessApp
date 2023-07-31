from main5 import ForgotPassword
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.factory import Factory
from py_screens import *
from kivy.uix.modalview import ModalView
from kivy.app import App


class ForgotPasswordApp(ForgotPassword, MDApp):
    def build(self):
        Builder.load_file("forgot_password.kv")
        return ForgotPassword()

