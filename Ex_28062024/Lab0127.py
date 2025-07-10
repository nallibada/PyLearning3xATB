# Access modifiers in python
# Public, Private and Protected Access Specifiers
# Public members - Accessible anywhere from outside the class in which they are defined.This includes modifying the attribute via a method.
# Private members - Accessible only through the class, In which they are defined. This means that the private members can only be accessed and modified within the class, and not from outside.
# Protected members - Similar to private members, the only difference is that protected members can be accessed and modified by subclasses of the class in which they are defined.

class Car:
    name = None
    __pri_var= '123'  # private attribute
    _pro_pass = '456'  # protected attribute
    pubpass = '345'  #public attribute

    def __init__(self):
        print('Iam a constructor, I am called when object is created')

    def __private_method(self):
        print('This is a private method')

    def _protected_method(self):
        print('This is a protected method')

    def printName(self,__pri_var1): # public method
        print("Iam allowed because i am public")
        if self.__pri_var == '123' :
            print(f"Hi 123")
            print(f"Hi {__pri_var1} , This is public method")
    def printprivar(self):          #public method accessing class/instance variable which is private
        print("accessing pri var")
        if self.__pri_var == '123' :
            print(f"Hi {self.__pri_var}, accessing instance private variable through public method")
#This is end of class
alto = Car()
alto.pubpass = '3'  # This is class /instance variable which is accessed outside class and able to change it . It is prone to security treat.
print(alto.pubpass)
alto._pro_pass= '789'
print(alto._pro_pass)
alto._protected_method()
alto.printName(777)
alto.printprivar()
#alto.__private_method() - This method is not accessed outside the class, this can be only accessed by members with in the class
#alto.__pri_var -This is class variable/private is not accessed outside the class, this can be only accessed by members with in the class


# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0127.py
# Iam a constructor, I am called when object is created
# 3
# 789
# This is a protected method
# Iam allowed because i am public
# Hi 123
# Hi 777 , This is public method
# accessing pri var
# Hi 123, accessing instance private variable through public method