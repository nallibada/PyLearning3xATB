# Encapsulation
# Binding the data variable with methods
# Data members / Class variables
# Methods - def - functions with in a class
# Wrapping or binding of data members / variables with the methods - encapsulation
#  Hide the data members from other functions
# Hide the data members ( Class variables/instance variable) by using only the methods.

class Car:
    name = None
    password = '123'

    def __init__(self):
        print('Iam called when a object is created')

    def change_password(self):
        self.password = '456'

#Enc of class here
xuv=Car()
xuv.password='345' # This is class /instance variable which is accessed outside class and able to change it . It is prone to security treat.
print(xuv.password)
