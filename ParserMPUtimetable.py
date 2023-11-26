import requests
import configparser
import random, string
from DBMPU import *


config = configparser.ConfigParser()  # создаём объекта парсера
config.read("configfileMPU.ini")


def getJSON(group):
    headers = {
        'Referer': config["requests"]["referer"],
    }

    params = {
        'group': group,
        'session': config["requests"]["session"],
    }

    response = requests.get(config["requests"]["url"], params=params, headers=headers)

    if response.status_code != 200:
        return (6,)
    if group not in requests.get(config["requests"]["url0"]).text:
        return (4,)

    try:
        data = response.json()

    except json.JSONDecodeError:
        return (2,)
    return (1, data, hashlib.sha256(json.dumps(data).encode()).hexdigest())


import json
import hashlib

lesson_time = json.loads(config["schedule"]["timetable"])
import datetime
from icalendar import Calendar, Event, vText


def lessons_schedule(json_data, group):
    if json_data is None or type(json_data) != dict:
        return (5,)
    try:
        if "grid" in json_data:
            cal = Calendar()
            cal.add('prodid', '-//Google Ins//Google Calendar 70.9054//EN')
            cal.add('version', '2.0')
            cal.add('dtstart', datetime.datetime(datetime.datetime.today().year, 9, 1, 0, 0, 0))
            cal["X-WR-CALNAME"] = "Раписание пар политеха"
            cal["X_WR_TIMEZONE"] = "Europe/Moscow"
            for week_day in json_data["grid"]:
                for lesson_number in json_data["grid"][week_day]:
                    lessons = json_data["grid"][week_day][lesson_number]
                    for lesson in lessons:
                        if lesson["sbj"]:
                            dt = lesson["dt"]

                            lesson_name = lesson["sbj"]
                            teacher = lesson["teacher"]
                            location = lesson["location"]
                            place = lesson["auditories"][0]["title"]
                            type_lesson = lesson["type"]
                            if "href" in place: place = place[place.find("https"): place.find('target') - 2]

                            event = Event()

                            df = datetime.datetime.strptime(lesson["df"], '%Y-%m-%d')
                            if df.weekday() <= int(week_day) - 1:
                                inc_date = int(week_day) - 1 - df.weekday()
                            else:
                                inc_date = 7 - df.weekday() - 1 + int(week_day)

                            dt = datetime.datetime.strptime(lesson["dt"], '%Y-%m-%d')
                            event['uid'] = "20230901T" + lesson_time[lesson_number][0] + "/" + str(week_day) + ''.join(
                                random.choice(string.ascii_lowercase) for i in range(5))
                            event.add('summary', vText(lesson_name, encoding='utf-8'))
                            dtstart = (df + datetime.timedelta(days=inc_date)).replace(
                                hour=int(lesson_time[lesson_number][0][0:2]),
                                minute=int(lesson_time[lesson_number][0][2:4]))

                            event.add('dtstart', dtstart)
                            event.add('dtend', dtstart.replace(hour=int(lesson_time[lesson_number][1][0:2]),
                                                               minute=int(lesson_time[lesson_number][1][2:4])))
                            event.add('rrule', {'freq': 'weekly', "interval": 1, 'until': dt})
                            event.add('location', vText(location + " " + place, encoding='utf-8'))
                            event.add('description', vText(type_lesson + "; " + teacher, encoding='utf-8'))
                            cal.add_component(event)

            cal.to_ical()
            file_path = config["file"]["path"]
            f = open(file_path + group + '.ics', 'wb')
            f.write(cal.to_ical())
            f.close()

            full_file_path = file_path + group + '.ics'
            link = config["file"]["output_link"] + group + ".ics"
            addLink(group, link, hashlib.sha256(json.dumps(json_data).encode()).hexdigest(), full_file_path)

        return (1, link)
    except Exception as e:
        return (2, e)


# data = getJSON("211-361")
# print(lessons_schedule(data, "211-361"))

def timetableParser(group):
    data = getJSON(group)

    # print("json", data[0])

    if data[0] != 1:
        return data
    # print(lessons_schedule(data[1], group))
    return lessons_schedule(data[1], group)
