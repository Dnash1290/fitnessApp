from .libaries import Screen
from .popup import PopWindow
from . import db

def data_valid(name, surname, username, password, confirmpass):
    check = ""
    if all(variable != "" for variable in [
        name, surname, username, password, confirmpass
    ]):
        if name.isalpha() and surname.isalpha():
            usernamedb = db.data.execute(f"""
            SELECT USERNAME FROM ACCOUNT
            WHERE USERNAME = '{username}';                
            """)
            if username != usernamedb:
                if password == confirmpass:
                    check = "new account made"
                    #adds the user information to database
                    db.make_new_user(name, surname, username, password)
                    
                else:
                    check = "confrim password not matched"
            
            else:
                check = "username already exists"
                
        else:
            check ="""
            name and surname can't
            have numbers in them
            """
    else: 
        check = "dont leave any fields blank"

    return check

class NewUser(Screen):                                         #this function calls the popwindow class in new user class
    def openpopup(self):
        pops = PopWindow()
        pops.open()
            
    def newacc(self):                         #this function handles the log in UI og the log in page
        name = self.ids.newname.text
        surname = self.ids.newsurname.text
        usernameid = self.ids.newuser.text
        passwordid = self.ids.newpass.text
        confirmpass = self.ids.confirmpass.text
        
        check = data_valid(name,surname, usernameid, passwordid, confirmpass)   #imported function to vaild user input
        if check != "new account made":
            self.ids.error_label.text = check
        else: 
            self.openpopup()                 
