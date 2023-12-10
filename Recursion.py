#Recursion Function
# Syntax 
# def recurse():
#     ---------
#     recurse()
#     --------
# recurse()

#Creat a factorial
# def factorial(n):

#     #base case
#     if n == 0:
#         return 1
#     #recursive case
#     fact = n * factorial(n-1)

#     return fact

# n = int(input("Enter the value n:"))
# print(factorial(n))

#Write a program to Print numbers from n to 1.
# def number(n):
#     if n==0:
#         return
#     print(n)
#     number(n-1)
# number(5)


#Write a program to P rint sum from 1 to n.
# def sumNumber(n):
#     if n ==1:
#         return 1
#     ans = n + sumNumber(n-1)
#     return ans

# n = int(input("Enter the value of n:"))
# print(sumNumber(n))

# Make a function which calculates the factorial of n using recursion.
# def factorial(n):
#     if n == 0:
#         return 1
#     fact = n * factorial(n-1)
#     return fact

# num = int(input("Enter the number:"))
# print(factorial(num))

#Make a function which calculates 'a' raised to the power 'b' using recursion.
# def power(a,b):
#     if b == 0:
#         return 1
    
#     ans = a * power(a,b-1)
#     return ans

# a = int(input("Enter the value of a:"))
# b = int(input("Enter the value of b:"))
# print(power(a,b))


#Make a function which calculates Fibonacci sequence using recursion.
# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Enter n:"))
# for i in range(1,n+1):
#    print(fibonacci(i))
