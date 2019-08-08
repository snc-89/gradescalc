from gpa import GPA
from assessmentv3 import *

grade = [0,2,8,1]
grade[2] = grade[2] + 3
grade[3] = grade[3] + 1
myGpa = GPA(grade)
print(myGpa.calcGPA())

print("237")


print("247")
mark = 8.5+6.68+7.05+9.18+10+9
print(mark)
cexam = Assessment(mark,60,60)
attend = Assessment(10,10,10)
assone = Assessment(12,15,15)
asstwo = Assessment(13.25,15,15)
comp247 = Unit(cexam,attend,assone,asstwo)
comp247.marksNeededInExam()
print("final unit total: " + str(comp247.unitTotal()))
