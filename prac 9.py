from logging import root
class student(object):
    def __init__(self,name,rollno):

       self.name=name
       self.rollno=rollno
class exam(student):
     def __init__(self,name,rollno,marks):
         super().  __init__(self,name,rollno)
         self.marks=marks
class result(exam):
     def __init__(self,name,rollno,marks):
         super().  __init__(self,name,rollno,marks)
         self.result=marks
         self.total_marks=self.result/600*100

     def display(self):
         return self.percentage
s=result("HENA", 43, 575)
print(s.display())