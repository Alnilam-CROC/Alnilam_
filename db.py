# import sqlite3
# conn  = sqlite3.connect('dbMPUtimetable.db', check_same_thread=False)
# cursor = conn.cursor()
# '''
# def db_link(group_number: str, link: bytes):
#     cursor.execute('INSERT INTO dbMPUtimetable (group_number, link)  VALUES (?,?)', (group_number, link))
#     conn.commit()
# @bot.message_handler(content_types=['text'])
# def Group(message):
#     text=message.from_user.id
#     link_test='test'
#     db_link(group_number=text, link=link_test)'''
# '''try:
#     sqlite_connection  = sqlite3.connect("SQLiteStudio\\dbMPUtimetable.db", check_same_thread=False)
#     cursor.close()
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
# '''
import sqlite3
con = sqlite3.connect("dbMPUtimetable.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS timetable(
            group_n TEXT PRIMERY KEY,
            link TEXT,
            hash_json TEXT,
            file_path TEXT)
            ''')


def getLink(group_n: str, link: str,hash_json: str, file_path: str):
    con = sqlite3.connect("dbMPUtimetable.db")
    cursor = con.cursor()
    cursor.execute('INSERT INTO timetable (group_n, link, hash_json, file_path)  VALUES (?,?,?,?)', (group_n, link,hash_json, file_path))
    con.commit()
    con.close()

def getLinkDB(group_n: str):
    con = sqlite3.connect("dbMPUtimetable.db")
    cursor = con.cursor()
    cursor.execute('SELECT link FROM timetable  WHERE  group_n=(?)', (group_n,))
    rec=cursor.fetchall()
    if len(rec)!=0:
        return  (1,rec)
    else:
        return (0, )
    con.commit()
    con.close()
# db_link(34,20,'33','33')
# proverka(340,200,'33','33')
con.commit()
con.close()