class VWOLogin:
    def __init__(self,email,password,name):
        self.__email = email
        self.__password = password
        self.name=name

    def login_confirm(self  ):
        if self.__email == "abc@gmail.com"   and self.__password == 123 :
            print("Allowed")
            print (self.name,self.__email,self.__password)
        else :
            print ("Not Allowed")

#This is end of class

page1 = VWOLogin("abc@gmail.com",123 , "Pramod")
page1.login_confirm()