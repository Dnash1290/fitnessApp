from .libaries import Screen
from .popup import PopWindow
from . import db 

def set_new_pass(username, password, confirmpass):
    check = ""
    if password == confirmpass: 
        view = db.data.execute(f"""
        SELECT USERNAME FROM ACCOUNT
        WHERE USERNAME = '{username}';                
        """).fetchone() #checks if username is valid
        try:    
            usernamedb = view[0]
        except:
            usernamedb = None

        if username == usernamedb:
            check = "valid"  
            db.update_user_password(username,password)
        else:
            check = "username not found"
    else: 
        check = "confrim password not matched"
    
    print(check)
    return check

set_new_pass("john" ,"Pizza", "Pizza")

class ForgotPassword(Screen):
    def openpopup(self):
        pops = PopWindow()
        pops.open()

    def newpass(self):
        usernameid = self.ids.username.text
        confirmpassid = self.ids.confirmpass.text
        newpasswordid = self.ids.newpass.text
        check = set_new_pass(usernameid, newpasswordid, confirmpassid)
        if check != "valid":
            self.ids.error_label.pos_hint={'center_x': 0.5, 'center_y': 0.58}
            self.ids.error_label.text = check
        else:
            pass
            self.openpopup()