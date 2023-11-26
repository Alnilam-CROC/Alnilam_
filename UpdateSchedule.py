from ParserMPUtimetable import *

for value in get_hash&group():
    group = value[0]
    hashh = value[1]
    json_data = getJSON()
    if json_data is None or type(json_data) != dict:
        return (2,)
    else:
        if json_data[2] != hashh:
            lessons_schedule(json_data, group)