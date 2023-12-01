import sqlite3
try:
    con = sqlite3.connect("dbMPUtimetable.db")
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS timetable(
                group_n TEXT PRIMERY KEY,
                link TEXT,
                hash_json TEXT,
                file_path TEXT)
                ''')
    con.commit()
    con.close()
except (sqlite3.Error, sqlite3.Warning) as err:
    print((2,))

def get_hashgroup():
    try:
        con = sqlite3.connect("dbMPUtimetable.db")
        cursor = con.cursor()
        cursor.execute('SELECT group_n, hash_json FROM timetable')
        rec = cursor.fetchall()
        return (4, rec)
    except (sqlite3.Error, sqlite3.Warning) as err:
        return (2,)
    finally:
        con.commit()
        con.close()
    


def addLink(group_n: str, link: str,hash_json: str, file_path: str):
    try:
        con = sqlite3.connect("dbMPUtimetable.db")
        cursor = con.cursor()
        cursor.execute('INSERT INTO timetable (group_n, link, hash_json, file_path)  VALUES (?,?,?,?)', (group_n, link,hash_json, file_path))
        return (3,)
    except (sqlite3.Error, sqlite3.Warning) as err:
        return (2,)
    finally:
        con.commit()
        con.close()

def giveLinkDB(group_n: str):
    try:
        con = sqlite3.connect("dbMPUtimetable.db")
        cursor = con.cursor()
        cursor.execute('SELECT link FROM timetable  WHERE  group_n=(?)', (group_n,))
        rec=cursor.fetchall()
        if len(rec)!=0:
            return  (1, rec)
        else:
            return (0, )
    except (sqlite3.Error, sqlite3.Warning) as err:
        return (2,)
    finally:
        con.commit()
        con.close()

def  deleteGroup(group_n:str):
    try:
        con = sqlite3.connect("dbMPUtimetable.db")
        cursor = con.cursor()
        cursor.execute('DELETE FROM timetable  WHERE  group_n=(?)', (group_n,))
    except (sqlite3.Error, sqlite3.Warning) as err:
        return (2,)
    finally:
        con.commit()
        con.close()