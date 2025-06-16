#python calculator
import math
print("*************This is the calculator******************")
value1 = float(input("Enter the value of 1st: "))
operation = input("Enter your operation + - * / % :")
if operation =='+':  #addition function
    value2 = float(input("Enter the value of 2st: "))
    ans = value1 + value2
    print(f"answer of addition value is: {round(ans)}")
    while operation =='+':
        value =float(input("Enter the new value: "))
        result=ans+value
        print(f"Result of addition value is: {round(result)}") 
elif operation =='-': #subartion function
    value2 = float(input("Enter the value of 2st: "))
    ans = value1 - value2
    print(f"Answer of subartion value is: {ans}")
    while operation =='-':
        value =float(input("Enter the new value: "))
        result=ans-value
        print(f"Result of subartion value is: {result}") 
elif operation =='*': #multiplication function
    value2 = float(input("Enter the value of 2st: "))
    ans = value1 * value2
    print(f"answer of multiplication value is: {ans}") 
    while operation =='*':
        value =float(input("Enter the new value: "))
        result=ans*value
        print(f"Result of multiplication value is: {result}") 
elif operation =='/': #divison function
    value2 = float(input("Enter the value of 2st: "))
    ans = value1 / value2
    print(f"answer of division value is: {ans}") 
    while operation =='*':
        value =float(input("Enter the new value: "))
        result=ans/value
        print(f"Result of divison value is: {result}") 
elif operation =='%': #modulodivison function
    value2 = float(input("Enter the value of 2st: "))
    ans = value1 % value2
    print(f"answer of modulo division value is: {ans}") 
    while operation =='%':
        value =float(input("Enter the new value: "))
        result=ans*value
        print(f"Result of multiplication value is: {result}") 
else:
    
    print(f"It's {operation}the invaild operator")
    





