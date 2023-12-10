# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
#     )
# cur = conn.cursor()
# sql="CREATE TABLE IF NOT EXISTS person(
#     id INT PRIMARY KEY,
#     name VARCHAR(250),
#     age INT,
#     gender CHAR)")
# 
#cur.execute(sql)
# conn.commit()

# for i in cur:
#     print(i)

# n = 3
# if n %2 != 0:
#     print("Weird")

    
# elif n %2 ==0:
#     for i in range(2, 5):
#         print(i, "Not Weird")

# elif n %2==0:
#     for row in range(6, 20):
#         print(row)
        
# elif n %2 ==0 and n>20:
#     print("Not Weird")
    
# else:
#     print("Invalid...")
