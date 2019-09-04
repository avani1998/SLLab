class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;

p1= Person("Supandi",14)
print("Name of the person is:", p1.name)
print("Age of the 1st perosn is", p1.age)
print(p1)
print("printing after deleting one attribute of p1")
del p1.age
print("\n Name of the person is", p1.name)
del p1
print("print name of the person is", p1.nam2) #gives error
