a = int(input('Enter the value of a:'))
b = int(input("Enter the value of b: "))

try:
    result = a / b

except ZeroDivisionError:
    result = None
    print("Error:Can't divided by zero")
    
finally:
    print("Division operation is completed:", result)