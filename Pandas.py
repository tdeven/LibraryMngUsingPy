# Pandas is a powerful and open-source library Python library for data manipulation and analysis, 
# providing data structures and functions for efficient operations.
    
# Table of Content
# Pandas Data Structures
# Pandas Series
# DataFrame

# Pandas Series-->A Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
# import pandas as pd
# import numpy as np

# #Creating empty series
# ser = pd.Series()
# print("Pandas series:", ser)

# #Simple arrary
# data = np.array(['D','E','V','E','N'])

# ser = pd.Series(data)
# print("Pandas Series:\n", ser)


# import pandas as pd

# a = ["Devendra", "Roshan","Rajesh","Paragash"]

# thakur = pd.Series(a)
# print(thakur[1])
# print(type(thakur[1]))
# print(len(thakur[1]))

# import pandas as pd

# arr = {
#     "Name" : ["Devendra","Roshan","Rajesh","Paragash"],
#     "Age" : [16,17,15,12],

# }

# result = pd.DataFrame(arr)
# print(result)


#--------------------------------------------------------------------------------------------

# import pandas as pd#pd is alias.alias means a new name of any thing

# mydata = {
#     'mycar' : ['BMW','Volvo',"ford"],
#     'passing' : [3,4,2]
# }

# myvar = pd.DataFrame(mydata)

# print(myvar)

# print(pd.__version__)#TO check the version of pandas

#Create a labels with the index argument
# import pandas as pd 

# a = [1,2,3,4,5]

# arr = pd.Series(a,index=["x","y","z","u","v"])
# print(arr)
# print(arr["z"])

#Key/Value Objects as Seriesj-->like directory , when creating a series
# import pandas as pd

# calories = {"day1":180, "day2":250, "day3":150, "day4":190}

# result = pd.Series(calories,index=["day5","day2"])
# print(result)

#-------------------------------------------------------------------------------------------------------------------
#DataFrame-->Data sets in Pandas are usually multi-dimensional tables,called DataFrames.
#Series is like a column, a DataFrame is the whole table.
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array,or a table with rowsa and columns.
#For example:-

# import pandas as pd

# data = {
#     'calories' : [400,200,300,490, 678],
#     'duration' : [50,60,80,70,100]
# }

# data_result = pd.DataFrame(data)
# print(data_result)

#Locate Row-->Pandas use the loc attribute to return one or more specified row(s).
# import pandas as pd

# data = {
#     'calories' : [400,200,300,490, 678],
#     'duration' : [50,60,80,70,100]
# }

# data_result = pd.DataFrame(data,index=["day1","day2","day3","day4","day5"])
# # print(data_result)
# # print(data_result.loc[[1,2,4]])#[]-->the result is a Pandas DataFrame
# print(data_result.loc["day4"])

#----------------------------------------------------------------------------------------------
#Load Files Into a Dataframe

# import pandas as pd

# df = pd.read_csv('data.csv')
# print(df.to_string())#Use to_string() to print the entire DataFrame


# import pandas as pd

# print(pd.options.display.min_rows)


#Pandas Read JSON
# import pandas as pd

# data = {
#     "Duration":{
#         "0":60,
#         "1":60,
#         "2":60,
#         "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# rt = pd.DataFrame(data)
# print(rt.info())

# import pandas as pd

# result = pd.read_csv("C:\\Users\MSI0\\Desktop\\PyProgramming.py\\Daily.csv")
# print(result)

#Read the csv file from directory
# import csv

# file = open("C:\\Users\MSI0\\Desktop\\PyProgramming.py\\Daily.csv")
# type(file)

# csvreader = csv.reader(file)

# header = []
# header = next(csvreader)
# header

#--------------------------------------------------------------------------------------
#Reading and writing the csv files 
# import pandas as pd

# print("Dialy spenses of the student")
# print()
# result = pd.read_csv("C:\\Users\MSI0\\Desktop\\PyProgramming.py\\Daily.csv")
# # data = result.dropna() #dropna ()-->This method returns a nex DataFrame, and will not changel the original
# # data = result.dropna(inplace= True) #dropna(inplace= True)--> will not return a new dataframe, but it will remove all rows containing NULL value from original
# data = result.fillna(13000.00, inplace= True)#Fillna()--> to replace empty cells with a value:
# print(data


#--------------------------------------------------------------------------------------------
# import pandas as pd

# rt = pd.read_csv("C:\\Users\MSI0\\Desktop\\PyProgramming.py\\Daily.csv")

# dt = rt.describe()
# print(dt)
# import seaborn as sns
# data = sns.__version__
# print(data)

