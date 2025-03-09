import day 
from datetime import time
from datetime import datetime

missingCourseSections = {"CPSC 121 Lecture", "CPSC 121 Lab", "CPSC 210 Lecture", "CPSC 210 Lab", "MATH 101 Lecture", "MATH 101 Discussion", "CHEM 123 Lecture", "CHEM 123 Lab"}
addedSections = {}
daydict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}
courses = [{"course": "CPSC 210", "section": 101, "activity": "lecture", "term": 1, "starttime": time(12, 30), "endtime": time(14, 00), "days": ["Monday", "Wednesday", "Friday"]}, 
           {"course": "CPSC 221", "section": 101, "activity": "lecture", "term": 1, "starttime": time(10, 30), "endtime": time(11, 00), "days": ["Monday", "Wednesday", "Friday"]}, 
           {"course": "CPSC 121", "section": 101, "activity": "lab", "term": 1, "starttime": time(10, 30), "endtime": time(11, 00), "days": ["Tuesday", "Thursday", "Friday"]}]

monday = day.Day("Monday")
tuesday = day.Day("Tuesday")
wednesday = day.Day("Wednesday")
thursday = day.Day("Thursday")
friday = day.Day("Friday") 

allDays = [monday, tuesday, wednesday, thursday, friday]

# add possible courses for each day
for course in courses: 
    for d in course["days"]:
        idx = daydict.get(d)
        allDays[idx].allSections.append(course) 

# sort courses by increasing end time
def sortTime(d):
    d.allSections = sorted(d.allSections, key=lambda section: section["endtime"])

for d in allDays: 
    sortTime(d)
    while len(d.allSections) != 0:
        currSection = d.allSections[0]

        if (len(d.mustSections) != 0):
            if (currSection in d.mustSections):
                d.schedSections.append(currSection)
                d.allSections.remove(currSection)
                d.mustSections.remove(currSection) 
            else: 
                overlap = False
                for mcourse in d.mustSections:
                    if ((mcourse["starttime"] <= currSection["starttime"] < mcourse["endtime"]) or 
                        (mcourse["starttime"] < currSection["endtime"] <= mcourse["endtime"])):
                        d.allSections.remove(currSection)
                        overlap = True
                        break
                if (overlap == False):
                    d.allSections.remove(currSection)
                    d.mustSections.remove(currSection)
        else:
            d.allSections.remove(currSection)
        print(currSection["course"])
        print(currSection["starttime"])
        print(currSection["endtime"])












