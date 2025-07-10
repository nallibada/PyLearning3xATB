class MyClass:
    def __init__(self):
        self.name = "Amit"
        self.__email = "Amit123@gmail.com"

    def public_func(self):
        print("Public func()")
    def __private_func(self):
        print("this is private method, you can only access me via another public method public_fn_accessing_private")
        print(self.__email)

    def public_fn_accessing_private(self):
        self.__private_func()

p = MyClass()
p.public_func()
p.public_fn_accessing_private()

#Security -> Not everyone can access your variables , methods