class A:
    def method(self):
        return "methodA"

class B:
    def method(self):
        return "methodB"

class C(A,B):
    pass

c = C()
print(c.method())
