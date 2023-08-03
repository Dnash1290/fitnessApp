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
                USERNAME VARCHAR(255) ,
                PASSWORD VARCHAR(255),
                PRIMARY KEY('USERNAME'));
                """
            self.mouse.execute(table)
        except:
            print("database is already been made")

        #script_directory = os.path.dirname(os.path.abspath(__file__))
        #db_path = os.path.join(script_directory, "app_database.db")


    def get_user(self, username):  #used by login button
        print("getting user data....") #gets user password
        view = self.mouse.execute(f"""
        SELECT PASSWORD FROM ACCOUNT    
        WHERE USERNAME = '{username}';         
        """).fetchone()
        try:
            password = view[0]   #gets password
            print(type(password)) #stores tuple as string
            
        except:
            password = None

        return password   
    
    
    def update_user_password(self,username,password):  #used by forgot passeword screen
        view = self.mouse.execute(f"""
        UPDATE ACCOUNT SET PASSWORD ='{password}'
        WHERE USERNAME = '{username}'; 
        """).fetchone()
        self.data.commit()
    
    def make_new_user(self, name, surname, username, password):
        print("stroing data...")
        self.mouse.execute(f"""
        INSERT INTO ACCOUNT VALUES(
            '{name}',
            '{surname}',
            '{username}',
            '{password}')
            """)
        print(f"new user {username} is added")
        self.data.commit()

        


#d.make_new_user("Yuri","Jahad","Jayuri","swordofjahadismine")
                #name surname username and password



