#from database_manager import database
#db = database()

def check_log(username, password):
    #db.get_user_info(username, password)
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
        
    print("sdfa")    
    print(check)
    print(type(check))
    return check
                
