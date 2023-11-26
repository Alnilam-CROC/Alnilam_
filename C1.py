from ParserMPUtimetable import *
from db import *

def giveLink(group):
    """Это функция предназначена для возврата ссылки на файл ics для даннной группы"""
    link = getLinkDB(group)
    if link[0] == 0:
        link = timetableParser(group)
        if link[0] == 4: return (1, )
        elif link[0] == 2 or link[0] == 3 or link[0] == 5: return (2, link[1])
        elif link[0] == 6: return (3,)
        else: return (5, link[1])
    if link[0] == 1:
        return (5, link[1])
# print(giveLink("211-361"))
