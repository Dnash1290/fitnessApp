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
    i = 3

    def login(self):
        usernameid = self.ids.username.text
        passwordid = self.ids.password.text
        person, password = "Aden", "password123"
        if usernameid != person and passwordid != password:
            error = self.ids.error_label
            error.text = f"""
            wrong password or username
                you have {self.i} chances"""
            self.i -= 1
            if self.i < 0:
                MyApp().close_app()
        else:
            print(usernameid, passwordid)

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
    
    def close_app(self):
        self.stop()

if __name__ == "__main__":
    MyApp().run()
