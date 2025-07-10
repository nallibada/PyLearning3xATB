#Multilevel inheritanc
class Grandfather: #parent class /base class
    _key= "abc@123"
    def __init__(self):
        print(self._key)
    def grandfather_fn(self):
        return "grandfather method"

class Father(Grandfather): #Child class / sub class
    def Father_fn(self):
        return "Father method"

class Child(Father): #Child class / sub class
    def Child_fn(self):
        return "Child method"

f1=Father()
print(f1.grandfather_fn())
print(f1.Father_fn())
print(f1._key)
gf=Grandfather()
print(gf._key)
c1 = Child()
print(c1.grandfather_fn())
print(c1.Father_fn())
print(c1.Child_fn())
