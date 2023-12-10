#What an Why?-->They are blocks of reusable code that performs a specific task.


# def sumOneToN(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum+=i
#     return sum

# n = int(input("Enter a n:"))

# output=sumOneToN(n)
# n1 = int(input("Enter a n1:"))
# output1 = sumOneToN(n1)
# print("The sum of all number:", output,output1)

#Types of functions
# 1.Built-in
# 2.User defined

#Write a function that prints hello world
# def printHello():
#     print("Your LuLu is small")
# printHello()

#Types of arguments
# 1.Default argument
# 2.Keyword argument (named arguemnts)
# 3.Positional arguments
# 4.Arbitrary arguments(variable-lenght argument *args and *kwarrs)

# def add(n1,n2=0):
#     print("n1:",n1)
#     print("n2:",n2)
#     sum = n1 + n2
#     return sum

#Positional arguament
# print("The sum is=", add(2,3))

#Keyword argument(name arguments)
# print("The sum is=", add(n1=2,n2=3))

#Default argument
# print("The sum is=", add(0))

#Arbitrary arguments
# def addAllNumber(*args):
    #args -> tuple

# def addAllNumber(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# output = addAllNumber(1,33,33,4)
# print("sum:", output)

# def studentInfo(**kwargs):
#     for x,y in kwargs.items():
#         print(x,"is",y)


# studentInfo(name="Deven",age="22",city="Mangalbare")
# studentInfo(name="Rajesh",age="23",city="Japan")

#----------------------------------------------------------------------------------------------------------------#
#Nested Function
# def outer_function():
#     x = 1

#     def inner_function():
#         y = 2
#         result = x + y
#         return result
    
#     return inner_function()

# output = outer_function()
# print(output)
#Pass by reference and Pass by value

#pass by value
# def addOne(x):
#     x += 1
#     print("Inside Function:", x)
 
# x = 5
# addOne(x)
# print("Outside function:",x)

#pass by reference
# def modifyList(lst):
#     lst.append(2)
#     print("inside function:",lst)

# lst = [1,2,4]
# modifyList(lst)
# print("Outside function:",lst)

#-----------------------------------------------------------------------------------------------------------------#

#Adding two number program using function 
# def add():
#     x=int(input("Enter first number:"))
#     y=int(input("Enter second number:"))
#     sum = x + y
#     return sum

# output = add()
# print("The sum of two number in function is = ",output)

#STAR PATTERN 
#-----------------------------------------------------------------------------------------------------------------#
#Built-in Function
#Write a Python function to calculae the factorial of a number (a non-negative integer). The function accepts the 
#number as an argument.

def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    
    else:
        for i in range(1,n+1):
            ans *= i
    return ans   


n = int(input("Enter a n:"))

output = factorial(n)
print("The factorial is:",output)
