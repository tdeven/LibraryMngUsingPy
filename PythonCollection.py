#Python Collection(Arrays)
# 1. Lists
# 2. Tuple 
# 3. Set 
# 4. Dictionary

#Lists-->These allow us to store multiple item in a single variable.
# Fruits = ["Apple","Mango","Banana","Guave"]

# Lists = ["apple",1,2,"Raam"]
# for _ in Fruits:
#    print(Fruits)

# List Items

# Indexed-->Naming the variable i.e. Indexing the arrays
# Ordered-->User given values is same print no any change.
# Mutable-->We can update the list as their require.
# Duplicates allowed 
# Any datatype -->[1,4.1,"Ram",True,False,]
# Mix of different data types

# fruits = ["Apple","Mango","Cherry","Banana"]

# print(fruits) #How to print list

# print(type(fruits))#How to check type of list

# print(len(fruits))#How to check length of list

# #Checking if an item is present in the list
# if "Banana" in fruits:
#     print("Banana is part of the list")

# #Checking if an item is not present in the list
# if "kiwi" not in fruits:
#     print("Kiwi is not part of the list")

#Accessing items os a list
# e.g. list=[10,20,30,40]
# indexing-->0   1  2   3
# list[2]
 
#indexing-->list[2]
#Negative indexing-->list[-2]
#Range of indexes-->list[starting:ending]=[1:3]->[20,30]
#Range of negative indexes-->lists[-3,-1]

# fruits = ["Apple","Mango","Cherry","Banana"]

# print(fruits) #How to print list

#Indexing in list
# print(fruits[1])
# print(fruits[-2])
# print(fruits[-4:-1])
# print(fruits[1:3])

#Adding elements to a list
# 1. append()-->adds item to the end of the list e.g list=[10,20,30,40] 
# list.append(50)->list=[10,20,30,40,50]
# 2. insert()
# list.inset(2,60)->list=[10,20,60,30,40,50]
# 3. extend()--> list2 =[100,150]
# list.extend(list2)->list=[10,20,60,30,40,50,100,150]

# fruits.append("Kiwi")
# print(fruits)

# fruits.insert(2,"Kiwi")
# print(fruits)

# more_fruits = ["Guave", "Papaya"]
# fruits.extend(more_fruits)
# print(fruits)

#Removing elements from a list
# 1. Remove()--> list=[10,20,30,40]-->Remove specific item
#  list.remove(20)--> list=[10,30,40]
# 2. Pop()-->Remove item at given index or else last item
# list.pop(1)-->list=[10,30,40]
# list.pop()-->In this case last item remove. list=[10,20,30]

# fruits.remove("Banana")
# print(fruits)

# fruits.pop(2)
# print(fruits)

# fruits.pop()
# print(fruits)

#Changing item in a list
#list=[10,20,30]
#list[1]=40 --> list=[10,40,30]
# 1. At an Index -->list[1]=40 --> list=[10,40,30]
# 2. In a range -- list[1:3]=[40,50]

# fruits[1]="kiwi"
# print(fruits)

# fruits[1:3]=["Papaya"]
# print(fruits)

#Sorting a list-->list=[50,40,10,30,20]
# 1.Ascending-->list=[10,20,30,40,50]
# 2.Decending-->list=[50,40,30,20,10]

# fruits.sort()-->this is by default acending orders
# print(fruits)

# fruits.sort(reverse=True)#decending
# print(fruits)

# fruits.reverse()
# print(fruits)

#List Comprehension-->When we want to make a new lsit from item of an existing list.
# list=[40,20,30,10]
# for i in list:
#     if i>25:
#        newlist.append(i)  or

#        newlist=[i for i in list if i>25]

# new_fruits = [ fruits for fruits in fruits if "a" in fruits ]
# print(new_fruits)

#Copy a list
# new_fruits = fruits.copy()
# print(new_fruits)

# #Cancatenation a two list
# new_fruit = fruits + new_fruits
# print(new_fruit)

#Nested List
# list=[10,50,40,20,30]
# list[2]=[80,90]
# list[2][0]=80

# fruits.insert(2,["kiwi","papaya"])
# print(fruits)
# print(fruits[2][0])
     
#Some example of List 
#Given a list in Python and provided the index of the elements,Write a program to swap the two elemts in the list.

n = int(input("Enter size of the list:"))

list=[]
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index1:"))
idx2 = int(input("Enter index2:"))
print(list)

temp = list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp

print(list)