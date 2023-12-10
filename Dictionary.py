#Dictionary --> Story key-value pairs e.g.Phone Directory,Dictionary

#Creating a dictionary

# number = {
#     "Roshan" : 65066566,
#     "Rajesh" : 5555555,
#     "Devedra": [9809673105,9864212917]
# }

# Syntax
# dict1 = {
#     key1 : value1,
#     key2 : value2
#     -------------
#     -------------
#     keyn : valuen
# }

# Dictionary Items
# Ordered
# Changeable
# Unindexed
# Duplicate not allowed -->For Keys
# Any datatype

# numbers = {
#     "Roshan" : 65066566,
#     "Rajesh" : 5555555,
#     "Devendra": [9809673105,9864212917]
# }

# print(numbers)#Printing the dictionary
# print(type(numbers))#Check the type of dict.
# print(len(numbers))#Check the length of dict.

# #Access items of dict.
# print(numbers["Roshan"])
# print(numbers.get("Rajesh"))

# print(numbers.keys())

#upadate value in dict.
# numbers["Rajesh"] = 966696
# print(numbers)

#add element in dict
# numbers["Thakur"] =12525252
# print(numbers)

# more_numbers = {
#     "kia" : 5555555
# }

# numbers.update(more_numbers)
# print(numbers)

#Remove the elements from a dict
# numbers.pop("Devendra")
# print(numbers)

# numbers.popitem() #this will remove the last added item
# print(numbers)

# numbers.clear()#this will empty the dict
# print(numbers)

#printing elementof a dict
# for s,t in numbers.items():
#     print(s,t)

# Nested dictionaries
# number = {
#     "area1" : {
#         "x" : 0,
#         "y" : 1,
#         "z" : 2
#     },
#     "area2" :{
#         "a" : 3,
#         "b" : 4,
#         "c" : 5
#     }
# }

# print(number["area1"]['y'])
# print(number["area2"]['c'])

#Given a dictionary in Python, write a Python program to find the  sum of all items in the dictionary.

# dict = {
#     "a" : 800,
#     "b" : 200,
#     "c" : 300
# }
# print("The sum of dict values is:", sum(dict.values()))

#Give a string and a number N ,we need to mirror the characters from the N-th position up to the length of the string 
# in alphabetical order. In mirror operation,we change 'a' to 'z', 'b' to 'y' and so on.

#Zip function-->dict1 = dict(zip(l1,l2))

input_string = input("Enter a string:")
n = int(input("Enter a n:"))

#Creating a dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse = alphabets[::-1]
dict1 = dict(zip(alphabets,reverse))

#Finding the part of string on which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding the mirror string
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string
res = prefix + mirror
print("The result is:", res )