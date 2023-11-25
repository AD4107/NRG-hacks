import math

currentDate = int(input("What is today's day: "))
currentMonth = int(input("What is this month(in numbers): "))
dueDate = int(input("What day is due day: "))
dueMonth = int(input("What is the month this is due(in numbers): "))
hours = int(input("How many hours do you think you will spend on this assignment: "))


def remainingTime(cd, cm, dd, dm):
    if (cm == dm):
        return dd - cd
    else:
        if(cm > dm):
            totalD = 0
            while(dm != cm):
                totalD += getDaysInMonth(cm)
                cm += 1
                if(cm == 13):
                    cm = 0
            return (totalD + dd) - cd
            
        else:
            totalDay = getDaysInMonth(dm) + dd
            return totalDay - cd

def getDaysInMonth(m):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif m in [4, 6, 9, 11]:
            return 30
        elif m == 2:
            return 29
        else:
            return -1
        
time = remainingTime(currentDate, currentMonth, dueDate, dueMonth)
print("You have ", time, " days left to finish this assignment! ")
if (hours/time < 1):
    print("It is best that you spend ", (hours/time), " minutes per day to finish this assignment. ")
else:
    h = math.floor(time/hours)
    print("It is best that you spend ", h, " hours and ", (hours/time * 60) - h ,"minutes per day to finish this assignment. ")

