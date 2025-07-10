class Parent:
    gold ="2kg"

    def BHK2(self):
        print ("2BHK")

class child(Parent):
    def BHK3(self):
        print("3BHK")

c1 = child()
c1.BHK2()
c1.BHK3()
print(c1.gold)
