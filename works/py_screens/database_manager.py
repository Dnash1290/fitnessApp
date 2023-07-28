import sqlite3

class database:
    def __init__(self) -> None:
        self.data = sqlite3.connect("app_database.db")
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
            print("table aready created")           
        
    def get_user_info(self, username, password):
        view = self.mouse.execute(f"""
        SELECT PASSWORD FROM ACCOUNT
        WHERE USERNAME = '{username}';         
        """).fetchone()
        print(type(view))
        print(view)
        
    
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
database().get_user_info("jhyuf","awee23")