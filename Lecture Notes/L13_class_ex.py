# A class defines the attributes of an object
# The object is an "instance" of the class 

# By convention we capatilize class names 
class Square():
    
    # All functions in the class have to have self as the first argument 
    # the __init__ is our constructor 
    # This runs automatically when we make an object
    # We always have to provide a constructor 
    def __init__(self, w, h):
        # To define a variable for an object, we need to iniitilize the variable in the constructor
        # "self" is the variable that represents the current object 

        # Private variables and methods are not intended for a user to access
        # By convention we note private variables with a single leading underscore
        # Private methods are noted with two leading underscores

        # To define a variable 
        # self.variable_name = variable_name 
        self._w = w
        self._h = h
        self.__area() # This sets self.A 


        print("We're in the constructor")

    def __area(self):
        self._A = self._w * self._h 

    def print_properties(self):
        print("w:", self._w)
        print("h:", self._h)
        print("A:", self._A)


    # Setters 
    def set_h(self, h):
        self._h = h
        self.__area()

    def set_w(self, w):
        self._w = w
        self.__area()

    # Getters
    def get_A(self):
        return self._A 


    # destructor - This runs automatically when we delete an object
    # We don't always need a destructor 
    def __del__(self):
        print("We're in the destructor")

# To make an object, we use the class name like a function call 
square_1 = Square(1, 2)
square_2 = Square(3, 4)

square_2.set_h(20)

square_1.print_properties()
square_2.print_properties() 
print("A:", square_2.get_A())

