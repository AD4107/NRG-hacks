import math

# Global variables
numberOfCourses = int(input("What is the number of courses you're taking this semester? "))
finalMarks = []

# Functions for calculations
def courseAverage():
    totalW = 0
    totalM = 0
    totalG = 0
    keepRun = True
    while(keepRun):
        continueAssignments = input("Do you have an assignment mark and weighting to add? Yes or No ")
        while(continueAssignments.lower() == "yes"):
            assignment = float(input("State your assignment mark "))
            weighting = float(input("State the weighting for the assignment "))
            totalW +=  weighting
            totalM += assignment * weighting
            totalG += 1
            continueAssignments = input("Do you have another assignment mark and weighting to add? Yes or No ")
        keepRun = False
        if(totalW == 0):
            avg = "N/A"
        else:
            avg = (totalM / totalW)
        print('Course average:', avg)

    return avg

def overallAverage():
    totalFinalMarks = sum(finalMarks)
    overall = totalFinalMarks / numberOfCourses
    return overall

# Call functions
for i in range(numberOfCourses):
    courseAverage()
overallAvg = overallAverage()


# Collect final marks for each course
for i in range(numberOfCourses):
    finalMark = int(input("Input your final mark for course {}: ".format(i + 1)))
    finalMarks.append(finalMark)

print("Overall Average:", overallAvg)
