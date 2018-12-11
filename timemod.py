import time


def getnowtime():
    currentTime = current[11:16]
    return currentTime

current = str(time.asctime(time.localtime(time.time())))
currentDayname = current[0:3]
currentMonth = current[4:7]
currentDay = current[8:10]
currentTime = current[11:16]