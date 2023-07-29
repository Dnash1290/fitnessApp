
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.factory import Factory
from py_screens import *
from kivy.uix.modalview import ModalView
from kivy.app import App

Window.size = (360, 640)

class WindowManager(ScreenManager):
    pass


class Login(Screen):
    print("ran??")
    i = 3
    def login(self):
        usernameid = self.ids.username.text
        passwordid = self.ids.password.text
        check = logsys.check_log(usernameid, passwordid)
        if check:
            print("login in ")
        else:
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
                
        
class PopWindow(ModalView):
    pass


class NewUser(Screen):
    def openpopup(self):
        pops = PopWindow()
        pops.open()
            
    def newacc(self):
        name = self.ids.newname.text
        surname = self.ids.newsurname.text
        usernameid = self.ids.newuser.text
        passwordid = self.ids.newpass.text
        confirmpass = self.ids.confirmpass.text
        
        check = logsys.data_valid(name,surname, usernameid, passwordid, confirmpass)
        if check != "new account made":
            self.ids.error_label.text = check
        else: 
            self.openpopup()
            
            

            
class ForgotPassword(Screen):
    def newpass(self):
        usernameid = self.ids.username.text
        confirmpassid = self.ids.confirmpass.text
        newpasswordid = self.ids.newpass.text
        
        #if newpasswordid == confirmpassid:
            #alldata.update_user_info(usernameid,newpasswordid)

        #print(f"""

        #username: {usernameid}
        #new password: {newpasswordid}
        #confirm password: {confirmpassid}
        #""")


class MyApp(MDApp):
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
