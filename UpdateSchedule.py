from ParserMPUtimetable import *
from DBMPU import *

for value in get_hashgroup():
    if value[0] == 4:
        group = value[1][0]
        hashh = value[1]
        json_data = getJSON()
        if json_data[2] != hashh:
            lessons_schedule(json_data, group)
    else:
