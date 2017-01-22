import sqlite3
import os

basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = basedir + r'/UserDB.db'

cx = sqlite3.connect(dbpath, check_same_thread=False)
cu = cx.cursor()

class DataManage:
    @staticmethod
    def DataInsert(formc):
        sqlcmd = "INSERT INTO USERS(NAME, PSW, EMAIL, TEL) VALUES('%s', '%s', '%s', '%s')" % (formc['name'], formc['psw'], formc['email'], formc['tel'])
        cu.execute(sqlcmd)
        cx.commit()
        return True
    def DataSelect(formc):
        sqlcmd = "SELECT * FROM USERS WHERE NAME='%s' AND PSW='%s'" % (formc['name_l'], formc['psw_l'])
        cu.execute(sqlcmd)
        users_info = cu.fetchall()
        return users_info