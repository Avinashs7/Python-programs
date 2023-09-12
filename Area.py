import math
class shape:
    def __init__(self):
        self.area=0
        self.name=""
    def display(self):
        print("The area of ",self.name," is ",self.area)
class triangle(shape):
    def __init__(self,base,height):
        self.name="triangle"
        self.base=base
        self.height=height
    def calculateArea(self):
        self.area=self.base*self.height/2
class circle(shape):
    def __init__(self,radius):
        self.name="circle"
        self.radius=radius
    def calculateArea(self):
        self.area=3.142*self.radius**2
class Reactangle(shape):
    def __init__(self,width,height):
        self.name="rectangle"
        self.width=width
        self.height=height
    def calculateArea(self):
        self.area=self.width*self.height/2    
c=circle(15)
t=triangle(2,2)
c.calculateArea()
t.calculateArea()
c.display()
t.display()
