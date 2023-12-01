from ParserMPUtimetable import *
from DBMPU import *
if get_hashgroup()[0] == 4:
    for value in get_hashgroup()[1]:
        group = value[1][0]
        hashh = value[1][1]
        json_data = getJSON()
        if json_data[2] != hashh:
            lessons_schedule(json_data, group)
