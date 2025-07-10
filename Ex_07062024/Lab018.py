#STRINGS
# In build functions-
#Function -> To Repeat a task- you can use a function
#print(),input, type(),format(),max, min , id(),sum(),avg()

#Strings Functions
name='AMITAB BACHnan' # This indexed from 0 to len-1, 0 to 4, A,M,E,E,R
print (name)
print(type(name))
print(id(name)) #id -> memory address where it is stored 430432432
print(len(name)) #length of string .Always starts from (1)

name=name.upper()
print(name)
name=name.lower()
print(name)
name=name.casefold()
print(name)
name=name.capitalize()
print (name)
a=name.count('A')
print(a)
print(name[4])
print(name[-1])
#print(name[5]) #IndexError: string index out of range
print(name.casefold())
# In python,strings are immutable in nature. - We cannot change the individuals letters in a string once stored in memory, instead we can give completely new word.

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_07062024\Lab018.py
# Ameer
# <class 'str'>
# 2321540584224
# 5
# AMEER
# ameer
# ameer
# Ameer
# 1
# r
# r
# m
# Ame