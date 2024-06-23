# Task 2.1) Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
import math

num= float(input("Enter the number :"))
sq_of_num=math.pow(num,2)
cube_of_num=math.pow(num, 3)
print("The square of ",num," is ",sq_of_num)
print("The cube of ", num, " is ", cube_of_num)

#RESULT:
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_10062024\Task002_1.py
# Enter the number :2
# The square of  2.0  is  4.0
# The cube of  2.0  is  8.0
#
# Process finished with exit code 0