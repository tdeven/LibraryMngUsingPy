#lambda function-->function written in one line using lambda function accepts any number of arguments, but only has one expressions.
#Syntax: lambda parameters: expression
# def double(x):
#     return x * 2

# print(double(5))

double=lambda x:x*2
print(double(5))
multiply = lambda x,y:x*y
print(multiply(3,4))
add = lambda x,y,z:x+y+z
print(add(1,3,4))
full_name = lambda first_name, last_name : first_name+" " + last_name
print(full_name("DEVENDRA","THAKUR"))
age = lambda age: True if age >= 18 else False
print(age(19))


#----------------------------------------------------------------------------------------------

#map()--> applies a function to each item in an iterable(list,tuple , etc.)
#map(function,iterable)

store = [("shirt",23.00),
         ("paint",34.00),
         ("coat",43.00),
         ("vest",12.00)]

to_rupess = lambda data: (data[0], data[1]*1.32)
to_dollars = lambda data: (data[0], data[1]*1.32)
store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)

print()

#---------------------------------------------------------------------------------------------------

#filter()--> creates a collection of elements from an iterable for which a function returns true
#filter(function, iterable)

friends = [("Rajesh",19),
           ("Roshan",18),
           ("Rampargash",20),
           ("Anup",21),
           ("Anil",16)]

age = lambda data:data[1] >= 18
drinking_friends = list(filter(age, friends))

for i in drinking_friends:
    print(i)