#SETS -->Containers for storing multiple value in a variable
#Sets is used to represent by curly bracket
#e.g. names={"Ram","Rajesh","Roshan"}

#Set items
# Unordered-->not print in sequence
# Immutable-->Can't update existing values, but can remove , add.
# Unindexed
# Duplicates not allowed
# Any Datatype
# Mix of different data types

names={"ram" , "shayam" , "Dev"}
# print(names)
# print(type(names))
# print(len(names))

#Accessing item of set
# for x in names:
#     print(x)

#check if an item exist in a set
# if "Dev" in names:
#     print("Dev is part>")

#Adding element in set
# names.add("Devendra")
# print(names)

#Add another sequence in a set
# names_list=["Ria","Tia"]
# names.update(names_list)
# print(names)

#Remove element from a set
# names.remove("Tia")
# names.discard("Tia")#This function will not throw an error if value is not present in set
# print(names)

#Joining two sets
# s1 = {'a','b','c','d'}
# s2 = {'e','f','g','a'}
# print(s1,s2)

# s3=s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

#keep only duplicates while joining
# s1.intersection_update(s2)
# print(s1)

#Keep all values except duplicates
# s1.symmetric_difference_update(s2)
# print(s1)

#Given three arrays, we have to find common elements in three sorted lists using sets.

ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

s1s2=s1.intersection(s2)
final_set = s1s2.intersection(s3)

final_list = list(final_set)
print(final_list)

 


# t1 = tuple(ar1)
# print(t1)
