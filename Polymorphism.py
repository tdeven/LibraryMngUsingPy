#Example of Polymorphism
# class Animal:
#     def speaks(self):#abstract mehtod which will be overweritten
#         pass

# class Dog(Animal):
#     def speaks(self):
#         print("Barks")

# class Cat(Animal):
#     def speaks(self):
#         print("Meow")

# class Cow(Animal):
#     def speaks(self):
#         print("Mooo")

# Dog1 = Dog()
# Cat1 = Cat()
# Cow1 = Cow()

# Dog1.speaks()
# Cat1.speaks()
# Cow1.speaks()

#Type of Polymorphism
#1.Compile-Time polymorphism-->i. Method overloading
                         #    ii.Operator overloading
#Method overloading
# class Add:
#     def sum(self,a,b):
#         print(a+b)
    
#     def sum(self,a,b,c):
#         print(a+b+c)

#Operator overloading
# class Complex_numberf:
#     def __init__(self,real,img):
#         self.real = real
#         self.img  = img

#     def __add__(self,other):
#         return Complex_numberf(self.real + other.real, self.img + other.img)
    
# c1 = Complex_numberf(1,2)
# c2 = Complex_numberf(3,4)
# c3 = c1 + c2
# print(c3.real, " + i", c3.img)

#Run-Time polymorphism--> Method overriding

#Abstraction --> allows us to focus on the "what", of an object rather than " how " of the object.