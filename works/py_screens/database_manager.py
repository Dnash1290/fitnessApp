import sqlite3
import os

class database:
    def __init__(self) -> None:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_directory, "app_database.db")
        self.data = sqlite3.connect(db_path)
        self.mouse = self.data.cursor()

        try:
            table ="""
                CREATE TABLE ACCOUNT(
                NAME VARCHAR(255), 
                SURNAME VARCHAR(255),
                USERNAME VARCHAR(255),
                PASSWORD VARCHAR(255));
                """
            self.mouse.execute(table)
        except:
            #print("table aready created")   
            pass        
        
    def get_user(self, username):
        print("getting user data....")
        view = self.mouse.execute(f"""
        SELECT PASSWORD FROM ACCOUNT
        WHERE USERNAME = '{username}';         
        """).fetchone()
        password = view[0]
        print(type(password))
        return password
        
    
    def check_user_info(self, name, surname, username,password):
        self.mouse.execute("")
        pass
    
    def update_user_info(self,username,password):
        self.mouse.execute("")
    
    def make_new_user(self, name, surname, username, password):
        print("stroing data...")
        self.mouse.execute(f"""INSERT INTO ACCOUNT VALUES(
            '{name}',
            '{surname}',
            '{username}',
            '{password}')
            """)
        self.data.commit()
        print("data sucessfully stored")
        
#database().make_new_user("dsa","gfsdg","jhyugf","awee23")
#database().get_user("tasin000")