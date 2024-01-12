# Description: The class "Triangle" contains properties and methods to calculate hypotenuse, perimeter, and area, and setter methods for the base and height instance values, and getters for all properties listed prior.
# Additionally, the class "RightTriangle" extends the Triangle class and changes the description of the class, as well as the methods for calculating hypotenuse, and perimeter. 
# Inputs: An object instantiation, with a base and height arguement
# Outputs: Base, Height, Hypotenuse, Perimeter, Area
# Tests: Base 3, Height 4; Base 4, Height 5; Base foo, Height foo; Base _, Height 7;

from math import sqrt

class Triangle: #CapitalizdWords Notation
    #foo = foo # This is an example of class attribute, which is the same value for all instances of the class
    # dunder methods start and end with "__", denote methods that are used to customize classes.
    def __init__(self, base, height): # Init method defines instance attributes of the object
        self.base = base # creates the attribute base and assigns the value base parameter to it.
        self.height = height

        self.output()

    def __str__(self): # instance method that returns "" when the Triangle class is printed
        return f"Standard Triangle"
   
    # Operations regarding properties of triangle
    def hypotenuse(self):
        return sqrt((self.base/2)**2 + self.height**2)
    
    def perimeter(self):
        return self.hypotenuse()*2 + abs(self.base)
    
    def area(self):
        return (self.base*self.height)/2
    
    def output(self):
        print('\n',self)
        print('Base:', self.getBase()) # access their instance attributes using dot notation.
        print('Height:', self.getHeight())
        print('Hypotenuse:', self.getHypotenuse())
        print('Perimeter:', self.getPerimeter())
        print('Area:', self.getArea())

    # setter and getter functions
    def setBase(self, input): # setters allow you to control how a variable is changed. for example, defining a type, or a range
        if input is type(float):
            self.base = input
            return None
        else:
            return f"Input '{input}' is not a float"
        
    def setHeight(self, input):
        if input is type(float):
            self.base = input
        else:
            return f"Input '{input}' is not a float"
    
    def getBase(self): # getters return the value of a instance variable or result of a instance method
        return self.base
    
    def getHeight(self):
        return self.height
    
    def getHypotenuse(self):
        return self.hypotenuse()
    
    def getPerimeter(self):
        return self.perimeter()
    
    def getArea(self):
        return self.area()

class RightTriangle(Triangle): # Class extends Triangle
    def __str__(self): # instance method that returns "" when the Triangle class is printed
        return f"Right Triangle"
    
    def hypotenuse(self):
        return sqrt(self.base**2 + self.height**2)
    
    def perimeter(self):
        return abs(self.base)+abs(self.height)+self.hypotenuse()
    
rightTriangle = RightTriangle(3, 4)

