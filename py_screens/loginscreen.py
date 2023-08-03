from .libaries import *
from . import db 

def check_user (username, password):
    check = False
    passworddb = db.get_user(username) #returns password
    if passworddb != None:  #if nothing is return that means that username is invalid 
        if password == passworddb:
            check = True

    return check


class Login(Screen):                    
    print("ran??")
    i = 3                                                                   
    def login(self):                    #this function handles the log in UI og the log in page
        usernameid = self.ids.username.text
        passwordid = self.ids.password.text
        check = check_user(usernameid, passwordid) #imported function to vaild user input
        if check:
            print(f"{usernameid} has login in ")                             
        else:                                               #outputs UI functionlty 
            if self.i <= 0:
                MDApp.close_app()    
                pass
            else:
                error = self.ids.error_label 
                error.text = f"""
                wrong password or username
                    you have {self.i} chances
                """
                self.i -= 1
               