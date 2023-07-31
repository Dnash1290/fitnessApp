print("libaries have been run!!!")
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from . import db


def check_log(username, password):
    db.get_user(username)
    check = False
    if password == "user1":
        check = True
    return check