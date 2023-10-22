class Student:
    def GetStudentData(self):
        self.rollno=int(input('enter roll no ='))
        self.name=input('enter name =')
class Test(Student):
    def MarksTest(self):
        self.sub1 = int(input('enter subject 1 marks ='))
        self.sub2 = int(input('enter subject 2 marks ='))
class Sport(Student):
    def SportsTest(self):
        self.sport = int(input('enter sports marks out of 50 ='))
class Results(Sport,Test):
    def ResultDisplay(self):
        print(f'Name Of Student is {self.name} and roll no is {self.rollno}')
        avg=(self.sub1+self.sub2)/2.0
        print('Average of test subjects is ',avg)
        print(f'Marks of Sports are {self.sport}')
p1=Results()
a=p1.GetStudentData()
b=p1.MarksTest()
c=p1.SportsTest()
d=p1.ResultDisplay()


