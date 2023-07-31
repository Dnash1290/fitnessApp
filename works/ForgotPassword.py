from libaries import Screen
from popup import PopWindow
from py_screens import *

class ForgotPassword(Screen):
    def openpopup(self):
        pops = PopWindow()
        pops.open()

    def newpass(self):
        usernameid = self.ids.username.text
        confirmpassid = self.ids.confirmpass.text
        newpasswordid = self.ids.newpass.text
        check = logsys.set_new_pass(usernameid, newpasswordid, confirmpassid)
        if check != "valid":
            self.ids.error_label.pos_hint={'center_x': 0.5, 'center_y': 0.58}
            self.ids.error_label.text = check
        else:
            pass




            self.openpopup()