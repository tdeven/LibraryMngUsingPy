#Strings
# name = 'Devendra'
# name2= "Kumar"
# name3 = '''Thakur'''

# print(name,name2,name3)

# print(type(name))
# print(len(name))

#Assigning multiline string to a variable.
#paragraph = '''This is a multiple string.
# You can write multiple lines within triple quotes.'''

#Array-like indexing in strings
# text = "Hello, world!"

# print(text[0])
# print(text[9])
# print(text[-11])
# print(text[8])

#Traversing a string
# for i in name:
#     print(i)

#Using list comprehension
# list = [char for char in name]
# for i in list:
#     print(i)

#find a char/substring in a string
# print(name.find("d"))

#String find()-->returns the index of first occurance of the character/substring
            #   -->return --1 if not found in original sring


#Slicing a string-->Used to get part of a string
# syntax:
# [start:end]
# x = name[2:5]
# print(x)

# x = name[:5]
# print(x)

# x = name[-4:]
# print(x)

#Modify String
# 1.upper()
# 2.lower()

#Converting upper case
# name = 'devendra'
# x = name.upper()
# print(x)

# name1 = "DEVENDRA"#lower case
# y = name1.lower()
# print(y)

# z = name.capitalize()
# print(z)

#For stripping/removing anr trailing whitespace
# name = "     Devendra   "
# u = name.strip()
# print(u)
# print(name)

#String replace()
# Syntax:
# string.replace(old_substring, new_substring, count-->No.of time)

# x = "Hellow world, I am Devendra"
# print(x.replace("Devendra","Deven",1 ))

#split()-->Used to split the string into a list of substring
# Syntax:
# string.split(sep=separator-->optionally, maxsplit-->how many time we want to split at the separtion )

# name = "Devendra, Kumar, Thakur"
# print(name.split(",",2))

#Concatenation the string
# str1 = "Hello World"
# str2 = "Welcome to python programming world"
# print(str1 + str2)

#format()-->Used to insert variable value in a string 
# student_name = input("Enter the name of the student:")
# student_marks = int(input("Enter the marks of the student:"))

# str1 = "The student name is {s}, and marks is {m}".format(s=student_name, m=student_marks)
# print(str1)

#Escape characters-->These are special characters that are used to respect some non-printable / return characters in string
# Code   Result
# \`--> Single Qoute
# \\ -->Backslash
# /n-->New line 
# \r--> Carriage return
# \t-->Tab 
# \b-->Backspace
# \f-->Form Feed 
# \ooo-->Octal Value 
# \xhh-->Hex value 


# text = "The expected always happens"
# print(text)
# print(len(text))
# print(text.find('pp'))
# print(text[:11])
# print(text.replace('always',"never"))
# text2 = "no matter what"
# new_text=text + text2
# print(new_text)

#Write a Python fucntion that checks if the gien string is a palindrome or not.
def palindrome(n):

    clean_n = n.replace(" ","").lower()

    reverse_n = clean_n[::-1]
    return clean_n == reverse_n

 
n = input("Enter the value of n:")
if palindrome(n):
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")