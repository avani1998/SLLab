#Create class called Student having name and age as attribute accept marks of student and create two objects of class. Define accept
#and display function for a class object
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("-"*20+"Details of student are"+"-"*20)
        print("The name of student is:",self.name)
        print("The age of student is:",self.age)
        print("The marks of student is:")
        for x in range(0,3):
            print(self.marks[x],end="")
    def accept(self):
        print("Enter the student details")
        self.name=input("Enter the name: ")
        self.age=int(input("Enter the age: "))
        self.marks=[int(x) for x in input("Enter three marks of students").split(" ")]
s3=Student("",0,[0,0,0])
s1=Student("Avani",20,[23,24,25])
s2=Student("Krisha",11,[21,22,23])
while(True):
    print()
    i=int(input("Enter your choice\t 1:Enter student details\t2:Display student details\t3:exit\n"))
    if i==1:
                s3.accept()
    elif i==2:
                s3.display()
    elif i==3:
                exit(0)
#or
#Student("Avani",21,[20,20,20]).display()
#Student("Krisha",11,[20,20,20]).display()
#s3=Student("",0,[0,0,0])
#s3.accept()
#s3.display()
