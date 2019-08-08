class GPA:
    def __init__(self, gradesList):
        self.gradesList = gradesList

    def calcGPA(self):
        total = 0
        count = 0
        for i in range(len(self.gradesList)):
            total = total + self.gradesList[i] * (i+4)
            count = count + self.gradesList[i]
        return total/count

    

    
