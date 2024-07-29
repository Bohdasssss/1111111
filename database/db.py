import aiosqlite 
import sqlite3


db_path = 'database.db'

class DataBase:
    def __init__(self,path) -> None:
        self.db_path = db_path

    async def add_user(self,user_id:int) -> None:
        async with aiosqlite.connect(self.db_path) as db :
            await db.execute('INSERT OR IGNORE INTO users VALUES (null,?)',(user_id,))
            await db.commit()

    async def select_all_users(self) -> None:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute('SELECT * FROM users') as cursor:
                return await cursor.fetchall()
            
    async def add_chanel(self,name:str,link) -> None:
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('INSERT INTO chanels VALUES(?,?)',(name,link,))
            await db.commit()
    
    def select_all_chanel_name(self):
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()
            res = cursor.execute('SELECT * FROM chanels').fetchall()
            all_chanel = list()
            for i in res:
                all_chanel.append(str(i[0]))

            return all_chanel
        
    
    def get_link(self,name):
        with sqlite3.connect(self.db_path) as db:
            return db.execute('SELECT link FROM chanels WHERE name=(?)',(name,)).fetchone()[0]
        
    def delete_chanel(self,name):
        with sqlite3.connect(self.db_path) as db:
            db.execute('DELETE FROM chanels WHERE link=(?)',(name,))
 
        

db=DataBase(path=db_path)

db.delete_chanel(name='https://t.me/getmyid_bot')
