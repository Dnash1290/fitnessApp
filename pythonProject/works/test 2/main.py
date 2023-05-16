from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

Window.size = (360, 640)


class LoginScreen(Screen):

    def login(self):
        usernameid = self.ids.username.text
        passwordid = self.ids.password.text
        print(f"this is username {usernameid} and this is password {passwordid}")

    def test(self, test):
        print(test)


class PassForgotSc(Screen):
    pass


class NewUser(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name="log"))
sm.add_widget(PassForgotSc(name="PassForgot"))


class MyApp(MDApp):
    def build(self):
        screen = Builder.load_file("my.kv")
        return screen


if __name__ == "__main__":
    MyApp().run()
