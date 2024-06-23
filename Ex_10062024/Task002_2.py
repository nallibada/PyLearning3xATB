# Task 2.2 ) Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1= float(input("Enter the first number :"))
num2= float(input("Enter the second number :"))
if num1 > num2:
    print("The first number is greater than the second number.")
    print(num1, "is greater than", num2)
if num1 < num2:
    print(num1, "is less than", num2)
if num1 == num2:
    print(num1, "is equal to", num2)

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_10062024\Task002_2.py
# Enter the first number :10.5
# Enter the second number :20.5
# 10.5 is less than 20.5
#-----------------------------------------------------------------
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_10062024\Task002_2.py
# Enter the first number :30.7
# Enter the second number :20
# The first number is greater than the second number.
# 30.7 is greater than 20.0
#-----------------------------------------------------------------
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_10062024\Task002_2.py
# Enter the first number :100
# Enter the second number :100
# 100.0 is equal to 100.0