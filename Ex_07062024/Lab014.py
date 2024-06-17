#Take the 2 int number from the user and we want to add them.
#we need to use the input() function.

    # num1=input('Enter the first number:')
    # num2=input('Enter the second number:''')
    # result=num1+num2
    # print(result)

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_07062024\Lab014.py
# Enter the first number:90
# Enter the second number:91
# 9091


#type conversion - str - >int->?int()
# + works as concatenation w.r.t strings
# + works as sum w.r.t integers
# int to str -> str()
#str to int -> int()
    # print(type(int(num1)))

num1=input('Enter the first number:')
num2=input('Enter the second number:''')
result=int(num1)+int(num2)
print(result)

result1=num1+num2
print(result1)
print(type(num1))
print(type(int(num1)))
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_07062024\Lab014.py
# Enter the first number:90
# Enter the second number:91
# 181
# 9091