from py_screens import *
from py_screens.libaries import *
from py_screens.ForgotPassword import ForgotPassword
from py_screens.NewUser import NewUser 
from py_screens.loginscreen import Login

Window.size = (360, 640)

class WindowManager(ScreenManager):
    pass
                

class MyApp(MDApp):        #adds all the kivy files together 
    def build(self):
        Builder.load_file("login.kv")
        Builder.load_file("new_user.kv")
        Builder.load_file("forgot_password.kv")
        wm = WindowManager()
        
        wm.add_widget(Login(name='login_screen'))
        wm.add_widget(NewUser(name='NewUser'))
        wm.add_widget(ForgotPassword(name="ForgotPassword"))
        return wm


if __name__ == "__main__":
    MyApp().run()
