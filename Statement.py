#Control Statement --> that allow us to control the flow of our program

#Conditional Statement

# if,if-else,elif
# Nested
#     Else if ladder
#     ternary
#     switch

# if condition: 
#     //statement 1
# else:
#     //statement2

#Take integer input and tell iif it is positive or negative
# number = int(input("Enter a number:"))
# if number >=0:
#     print("The number is positive:")
# else:
#     print("The number is negative:")

#Take positive interger input and tellif it is even or odd
# number = int(input("Enter the number:"))
# if number % 2 == 0:
#     print("The number is even number")
# else:
#     print("The number is odd number")


# '''#If cost price and selling price of an item is input throught the keyboard, write a program to determine 
#  wheateh the seller had made profit or incurred loss or no profit no loss.A lso determine how much profit 
#  he made or loss he incurred'''
# cost_price = int(input("Enter the cost price:"))
# selling_price = int(input("Enter the selling price:"))

# #if sp is more than cp -->profit
# if cost_price > selling_price:
#     Loss = cost_price - selling_price
#     print("We have incurred  loss of:",Loss)

# elif cost_price < selling_price:
#     profit = selling_price - cost_price
#     print("We have made profit:", profit)

# else:
#     print("We have made no profit and loss")


# Take input percentage of a  student and print the Garade according to marks:
# a. 81-100 Very Good
# b.61-80 Good
# c.41-60 Average
# d.<=40 fail

# marks = int(input("Enter the student marks obtained:"))
# if marks >=81:
#     grade = "Very Good"
#     print("The student is very good in study:", grade)
# elif marks >=61:
#     print("The student is not bad in study:")
# elif marks >= 41:
#     print("The student is average in study:")
# else:
#     print("Fail....")

#Multiple conditions Using 'and' and 'or'

# marks1 = int(input("Enter a marks1:"))
# marks2 = int(input("Enter a marks2:"))
# if marks1>50 and marks2>50:
#     print("Very good")
# elif marks1>50 or marks2>50:
#     print("Pass")
# else:
#     print("Fail")

#Take positive integer input and tell if it is a four digit number or not.
# number = int(input("Enter a number:"))

# if number >= 1000 and number <=9999:
#     print("Four digit number:")
# else:
#     print("Not four digit number:")

#Take 3 positive integers input and print the greatest of them.
# n1 = int(input("Enter first number:"))
# n2 = int(input("Enter second number:"))
# n3 = int(input("Enter third number:"))
# if n1>n2 and n1>n3:
#     print("The first number is greatest number.",n1)
# elif n2>n3 and n2>n1:
#     print("The second number is greatest number.",n2)
# else:
#     print("The third number is greatest number.",n3)

#Nested If-Else
#Find the greatest number among three number
# if n1 > n2:
#     if n1 > n3:
#         print("n1 is greatest",n1)
#     else:
#         print("n3 is greatest",n3)
# else:
#     if n2 > n3:
#         print("n2 is greatest", n2)
#     else:
#         print("n3 is greatest",n3)

#Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15.
# number = int(input("Enter the positive number:"))

# if number % 15 == 0:
#     print("Number is divisible by 15")
# else:
#     if number % 5 == 0 or number % 3 == 0:
#         print("Number is divisible by 5 or 3 but not by 15")
#     else:
#         print("Number is neither divisible by 3 nor by 5")

# Match Case --> Switch Case statement
# Syntax:
# match x:
#     case 1: statement1
#     case 2: statement 2
#      ......
#     case n: statement n

#Calculator
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number:"))

# operator = input("Enter a operator:")
# match operator:
#     case "+":
#         print("The sum is:", num1 + num2)
#     case "-":
#         print("The differenece is:", num1 - num2)
#     case "*":
#         print("The multiply is:", num1 * num2)
#     case "/":
#         print("The division is:", num1 / num2)
# #     case _:
#         print("Enter the valid operator:")

# Ternary Operator.
#Write a program to checkif number is odd or even using ternary operator.
# number = int(input("Enter a number:"))
# print("Output is", "Even" if number % 2 == 0 else "odd")   

#Loops
# a. For Loops
# b. While Loops

# For Loops
#  for i in range(1,10):
# for variable in range(start, stop , step)
#   //code

# num = int(input('Enter a number:'))
# for num in range(1,5,2):
#     print("Hello World")

# for _ in range(11):
#     print("I am sorry")

# Print elements of a list using for loop.
# list = [10,20,30,40,50,60]
# for i in list:
#     print(i)

#While loop -->Runs till a condition is true.
# i=0
# while i<10:
#     Code 
#     i +=1

# number = int(input("Enter the number:"))

# while number <= 100:
#     print(number)
#     number += 2

# j=0
# while j<=10:
#     print(j)
#     j = j+1

#Print the given pattern
# n = int(input("Enter the value of n:"))

# for _ in range(n):
#     print("*" * 5)


# n = 8
# for i in range(n):
#     for j in range(1,n+1):
#         print(j, end="")
#     print()


#print 
# 1 
# 12
# 123 
# 1234  

# num = int(input("Enter the number:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end="")  
#     print()

# A 
# A B 
# A B C 
# A B C D 

# n =input("Enter a number:")
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#     -->Using ASCII CODE for this program

#To print
#     1
#   1 2 3
#  1 2 3 4 5
# 1 2 3 4 5 6 7


# n = int(input("Enter a number:"))
# for i in range(1,n+1):
#     #Printing spaces
#     print(" " * (n-i), end="")

#     #Printing digits
#     for j in range(1,2*i):
#         print(j,end="")
#     print()



     