# Hybrid inheritance
#Multiple types of inheritance
# such as single
# multiple
# multi level inheritance
class A:
    def methodA(self):
        return "MethodA"

class B(A):
    def methodB(self):
        return "MethodB"

class C(A):
    def methodC(self):
        return "MethodC"

class D(B,C): #Multiple and Multilevel inheritance
    def methodD(self):
        return "MethodD"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_01072024\Lab0140.py
# MethodA
# MethodB
# MethodC
# MethodD