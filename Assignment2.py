class Student():
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = [100 , 100 , 100]

    def display(self):
        print("Name of student is:", self.name)
        print("Age of student is: ",self.age)
        print("The marks are:")
        print(self.marks[0])
        print(self.marks[1])
        print(self.marks[2])
        
    def accept(self):
        self.name = input("Enter the name")
        self.age = input("Enter the age")
        self.marks[0] = input("Enter the marks in 1st subject")
        self.marks[1] = input("Enter the marks in 2nd subject")
        self.marks[2] = input("Enter the marks in 3rd subject")
s1=Student("Akshay",25,[25,25,25])
while True:
    n=int(input("Enter your choice \n 1:Enter student details\n 2:Display student details\n 3:Exit\n"))
    if n==1:
        s1.accept()
    elif n==2:
        s1.display()
    elif n==3:
        exit(0)
    else:
        print("Invaid Input")
