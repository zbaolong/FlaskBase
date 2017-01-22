import sqlite3
import os

basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = basedir + r'/UserDB.db'

cx = sqlite3.connect(dbpath, check_same_thread=False)
cu = cx.cursor()

formc = {}
formc['name_l'] = 'abc'
formc['psw_l'] = 'def'

sqlcmd = "SELECT * FROM USERS WHERE NAME='%s' AND PSW='%s'" % (formc['name_l'], formc['psw_l'])

xx = cu.fetchall()

if xx == []:
    print(xx)