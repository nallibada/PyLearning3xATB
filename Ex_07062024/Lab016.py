# Strings
# ''  '', '""  "", '"""" """""" - String is bunch of characters

a = "Hello"
name='Harry is a good person'
name1="""Harry is a good person.
       he has a dog .
       he is doing job"""

print(a)
print(name)
print(name1)

#dir='C:\nomrusers\User\PycharmProjects'
#print(dir)
# #C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_07062024\Lab016.py
#   File "C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_07062024\Lab016.py", line 14
#     dir='C:\nomrusers\User\PycharmProjects'
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 12-13: truncated \UXXXXXXXX escape
# Raw string
dir=r'C:\nomrusers\User\PycharmProjects' #as there is \n in the folder path , it will consider and give some error , so mention r'' before string to make it raw string , so that it will print as it is.
print(dir)
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_07062024\Lab016.py
# C:\nomrusers\User\PycharmProjects

#Format of the string
first_name="Harry"
last_name="Potter"
print("Mr.",first_name," ",last_name)
#f is used for formatting it is used replace the values of he variables
print(f'Your name is {first_name} {last_name}')
#print("First name is {} and last name is {}".format(first_name,last_name))

# format function is used to replace the values of variables in the required places.
print("first name is {} and last name is  {} and middle name is {} ".format( first_name,last_name, 2020))
