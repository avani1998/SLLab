
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;

p1= Person("Supandi",14)
p2= Person("ramu",12)

print("Name of the person 1 is:", p1.name)
print("Age of the 1st perosn is", p1.age)
print("Name of the person 2 is:", p2.name)
print("Age of the second perosn is", p2.age)
p2.age=10

print("Modified age of person is:", p2.age)

