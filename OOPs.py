# class Student:
    
#     def set_name(self,name):
#         self.name= name
    
#     def get_name(self):
#         return self.name
    
# student1 = Student()
# student1.set_name("Devendra")
# print(student1.name)

#Write a Python class named Rectangle to represetn a rectangle shape.The clas hsould have the following functionalities.
# 1. A method named set_dimensions that tkes two parameters width adn height and sets the attributes of the rectangle ofject accordingly.
# 2. A method nameed area that calculates and returns the area of the rectangle.
# 3. A method named perimeter that calculates and returns the perimeter of the rectangle.
#Use this to crate objects of the class and print the width , height, area and perimeter

# class Rectangle:
#     def set_dimension(self, width, height):
#         self.height = height
#         self.width = width
#     def area(self):
#         return self.height * self.width
#     def perimeter(self):
#         return 2*(self.height + self.width)
    
# #Creating objects
# rectangle1 = Rectangle()
# rectangle1.set_dimension(12,5)
# print("The height and widht of rectangle are:",rectangle1.height , rectangle1.width)
# print("The area of rectangle is=",rectangle1.area())
# print("The perimeter of rectangle is=",rectangle1.perimeter())

#Class Constructor
# Syntax:
# Class Class_name:
# def __init__(self,parameter1,parameter2,....):
#     Initialize instance variables(attributes)here
# class Rectangle:
#     def __init__(self, width, height):
#         print(f"The width:{width} and height:{height} of rectangle")
#         self.height = height
#         self.width = width
#     # def area(self):
#     #     return self.height * self.width
#     # def perimeter(self):
#     #     return 2*(self.height + self.width)

# rectangle1 = Rectangle(2,3)
# rectangle2 = Rectangle(4,5)
# rectangle3 = Rectangle( 6,7)
# print(rectangle1)

#Argument-->
#Access Modifiers
# 1.Public-->
# 2.Protected
# 3.Private

#Public modifier
# class ABC:
#     def __init__(self):
#         self.public_attribut= None
#     def public_function():
#         pass
        

# obj1 = ABC()
# obj1.public_attribut()
# obj1.public_function()

#Private modifier
# class ABC:
#     def __init__(self):
#         self.__public_attribut= None
#     def __private_function():#this is a private function
#         pass

# obj1 = ABC()
# print(obj1.__public_attribut())

#Protected modifier
# class ABC:
#     def __init__(self):
#         self._protected_attribut= None
#     def _protected_function():#this is a protected function
#         pass

#-----------------------------------------------------------------------------------------------------------------#
#Inheritance
# Syntax:
# Class SuperClass:
#   -->Attributes and methods of the superclass go here

# Class SuperClass(SuperClass):
#   -->Attributes and methods of the superclass go here

# class Parent:
#     def __init__(self):
#         self.super_attribute = True
#         print("This is the parent class.")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("This is a child class.")
#         print(self.super_attribute)

# child1=Child()

# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity *100
#  If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintencance charge. So total fare for bus instance
#  will becomethe final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self,sitting_capacity):
        self.sitting_capacity = sitting_capacity
    
    def get_fare(self):
        return self.sitting_capacity * 100

class Bus(Vehicle):
    def __init__(self, sitting_capacity):
        super().__init__(sitting_capacity)
    
    def get_fare(self):
        Vehicle_fare = super().get_fare()
        maintenance_fare = 0.1 * Vehicle_fare
        total_fare = Vehicle_fare + maintenance_fare
        return total_fare
    
Vehicle1 = Vehicle(50)
print("Vehicle fare:", Vehicle1.get_fare())

Bus1 = Bus(50)
print("Bus fare", Bus1.get_fare())