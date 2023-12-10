#Tuples-->Used to store multiple items in a variable.
# It is to represent small bracket but list is used to square bracket.
# colours = ("blue","green","orange","purple")

#Tuple items

# 1.Ordered
# 2.Immutable-->We can't change the value as own required. OR can't change values
# 3.Duplicate allowed
# 4.Any datatype
# 5.Mix of different data type 

#Creating the tuples
colours = ("blue","green","orange","purple")

#Creating a tuple with 1 item -->always use coma
# fruit = ("apple",)
fruit = tuple(("apple"))

#Check type of tuple
# print(type(fruit))

#Check length of tuple
# print(len(fruit))

#Accessing items in tuple
# print(colours[2]) #positive indexing
# print(colours[-1])#Negative indexing
# print(colours[1:2])#range indexing
# print(colours[-1:])#Negative range indexing

# #Check if an item exists in tuple
# if "green" in colours:
#     print("Green is a part of tuple")

#Traverse the tuples
# for i in colours:
#     print(i)

#concatenates 2 tuples
# more_colours = ("red","raddish")
# colours = colours + more_colours
# print(colours)

#Unpacking a tuple--> to put multiple variable
# colours1 , colours2 = colours
# print(colours1,colours2)

#Reverse a tuple

input_tuple = (1,2,3,4,5,6)

list=[]

#adding reversed values in a list
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)
print(output_tuple)

