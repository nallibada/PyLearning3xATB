class Person:
    #Attributes
    name = None
    id = None
    age = None
    phone_number = None

    #Behaviour
    def walk(self):
        print("walking ")

    def return_walk(self) -> object:
        return "I am walking like hero"

    def talk(self):
        print("talking")

    def eat(self, name):
        print("I am a method!!")
        print("eating", name)


#Creating an object of the class
surya = Person()
surya.name = "Surya"
surya.id = 1
surya.age = 23
surya.phone_number = 1234567890
surya.walk()
surya.talk()
surya.eat("Biryani")
surya.return_walk()

rithika = Person()
rithika.name = "Rithika"
rithika.id = 2
rithika.age = 21
rithika.phone_number = 9876543211
rithika.walk()
rithika.talk()
rithika.return_walk()
