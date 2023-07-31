from py_screens import *
from py_screens.libaries import *
from py_screens.ForgotPassword import ForgotPassword
from py_screens.NewUser import NewUser 

Window.size = (360, 640)

class WindowManager(ScreenManager):
    pass


class Login(Screen):                    
    print("ran??")
    i = 3                                                                   
    def login(self):                    #this function handles the log in UI og the log in page
        usernameid = self.ids.username.text
        passwordid = self.ids.password.text
        check = libaries.check_log(usernameid, passwordid)    #imported function to vaild user input
        if check:
            print("login in ")                             
        else:                                               #outputs UI functionlty 
            if self.i <= 0:
                MyApp().close_app()    
                pass
            else:
                error = self.ids.error_label 
                error.text = f"""
                wrong password or username
                    you have {self.i} chances
                """
                self.i -= 1
                

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
