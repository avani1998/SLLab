class Rectangle:
    def __init__(self,length,bredth,height):
        self.length=length
        self.bredth=bredth
        self.height=height
    def area(self):
        a=self.length*self.bredth*self.height
        print('The area is ',a)
r1=Rectangle(2,4,6)
r1.area()
