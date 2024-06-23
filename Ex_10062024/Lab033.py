# Program - Calculate  the area of a circle
#input -> radius
#output -> area of circle
#formula -> area = pi*r^2

# data type
#input -> int or float -> float
#output > float
#Core logic -> pi*r*r=3.14
#Value of pi by using match.py , is a utility provided to us
import math

radius = float(input('''Enter the radius:\n'''))
print(math.pi)
area = math.pi*radius*radius
area1= math.pi*(radius**2)
area2=math.pi*(math.pow(radius,2))

print("area: ",area)
print("area1: ",area1)
print("area2: ",area2)

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_10062024\Lab033.py
# Enter the radius:
# 10
# 3.141592653589793
# area:  314.1592653589793
# area1:  314.1592653589793
# area2:  314.1592653589793