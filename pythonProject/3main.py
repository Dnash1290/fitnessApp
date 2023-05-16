from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window


Window.size = (360, 640)


class WindowManager(ScreenManager):
    pass


class LoginScreen(Screen):
    def login(self):
        usernameid = self.ids.username.text
        passwordid = self.ids.password.text
        print(usernameid, passwordid)

    def back(self):
        pass


class NewUser(Screen):
    def newacc(self):
        name = self.ids.newname.text
        surname = self.ids.newsurname.text
        usernameid = self.ids.newuser.text
        passwordid = self.ids.newpass.text
        confirmpass = self.ids.confirmpass.text

        print(f"""
        --------------------------------------------      
              
        name: {name}
        surname: {surname}
        username: {usernameid}
        new password: {passwordid}
        confirm password: {confirmpass}
        """)


class ForgotPassword(Screen):
    def newpass(self):
        usernameid = self.ids.username.text
        confirmpassid = self.ids.confirmpass.text
        newpasswordid = self.ids.newpass.text

        print(f"""

        username: {usernameid}
        new password: {newpasswordid}
        confirm password: {confirmpassid}
        """)

        pass


class MyApp(MDApp):
    def build(self):
        Builder.load_file("login.kv")
        Builder.load_file("new_user.kv")
        Builder.load_file("forgot_password.kv")
        wm = WindowManager()
        wm.add_widget(LoginScreen(name='login_screen'))
        wm.add_widget(NewUser(name='NewUser'))
        wm.add_widget(ForgotPassword(name="ForgotPassword"))
        return wm


if __name__ == "__main__":
    MyApp().run()
