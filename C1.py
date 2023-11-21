import ParserMPUtimetable

def giveLink(group):
    link = (0, ) # getLinkDB(group)
    if link[0] == 0:
        link = ParserMPUtimetable.timetableParser(group)
        # print("link is", link)
        if link[0] == 4: return 1
        elif link[0] == 2 or link[0] == 3 or link[0] == 5: return (2,)
        elif link[0] == 6: return (3,)
        else: return link[1]

print(giveLink("211-361"))