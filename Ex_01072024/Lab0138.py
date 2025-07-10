#Multiple inheritance

class Father:
    def father_money(self):
        return "5"
    def home(self):
        return "This is from the Father"

class Mother:
    def mother_money(self):
        return "2"
    def home(self):
        return "This is from the Mother"

class Child(Father,Mother):
    # def home(self):
    #     return "This is from the Son"
    pass
son = Child()
print(son.father_money())
print(son.mother_money())
print(son.home())
# Diamond Problem in Java is solved in python by setting priority , when all classes have a method with same name then first preference is given to child class method and next preference is
#given to the method in parent classes based on the priority given in class declaration.

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_01072024\Lab0138.py
# 5
# 2
# This is from the Father

