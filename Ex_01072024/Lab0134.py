# Inheritance - Acquiring attributes and behaviour ( Data members and Methods)

#Types of inheritance :
# 1. Single - A to B - 80% is used in both API Automation and Web Automation.
# 2. Multiple - A , B to C ( Mother, Father -> Children)
# 3. Multilevel - A -> B -> C ( Grandfather -> Father -> Son)
# 4. Hybrid -  [ A->B->D and A-> C -> D]  ; Parent -> Son / Daughter -> Grand Son / Granddaughter
# 5. Hierarchical [A-> B , A->C , A -> D] ; Parent to multiple children

# Example : 3 BHK -> Father -> Son /daughter
# Concept in Object oriented programming that allows a class (child class) to inherit the attributes and methods from another class ( Parent class)

#SINGLE INHERITANCE:
class Grandfather: #parent class /base class
    _key= "abc@123"
    def __init__(self):
        print(self._key)
    def grandfather_fn(self):
        return "grandfather method"

class Father(Grandfather): #Child class / sub class
    def Father_fn(self):
        return "Father method"

f1=Father()
print(f1.grandfather_fn())
print(f1.Father_fn())
gf=Grandfather()
print(gf._key)

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_01072024\Lab0134.py
# abc@123
# grandfather method
# Father method
# abc@123
# abc@123