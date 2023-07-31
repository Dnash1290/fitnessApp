from . import db

def check_log(username, password):
    db.get_user(username)
    check = False
    if password == "user1":
        check = True
    return check

def data_valid(name, surname, username, password, confirmpass):
    check = ""
    if all(variable != "" for variable in [
        name, surname, username, password, confirmpass
    ]):
        if name.isalpha() and surname.isalpha():
            if username != "user1":
                if password == confirmpass:
                    check = "new account made"
                    
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
                    
  
def set_new_pass(username, password, confirmpass):
    check = ""
    if password == confirmpass:
        if username == "john":
            check = "valid"
        else:
            check = "username not found"
    else: 
        check = "confrim password not matched"
    
    print(check)
    return check

set_new_pass("john" ,"Pizza", "Pizza")



    #alldata.make_new_user(name, surname, usernameid,passwordid)
    #alldata.make_new_user(name, surname, usernameid,passwordid)
    #alldata.get_user_info()