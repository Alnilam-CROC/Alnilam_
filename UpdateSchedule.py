from ParserMPUtimetable import *
from DBMPU import *

for value in get_hashgroup():
    group = value[0]
    hashh = value[1]
    json_data = getJSON()
    if json_data[2] != hashh:
        lessons_schedule(json_data, group)