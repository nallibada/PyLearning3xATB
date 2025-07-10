class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance += amount

    def __withdraw(self,amount):
        self.balance -= amount

    def __show_balance(self):
        print ("your balance is", self.balance)

    def if_you_are_auth(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")
    def if_you_are_auth_user(self, auth,amount):
        if auth:
            self.__show_balance()
            self.__withdraw(amount=amount)
            print("After withdrawal")
            self.__show_balance()
        else:
            print("Not Allowed")

jp_chase = BankAccount()
jp_chase.deposit(500)
secret_pass=input("Enter your PIN to see your balance")
if secret_pass == "1234" :
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

secret_pass1=input("Enter your PIN to withdraw")
your_amt=int(input("Enter the amount to withdraw"))
if secret_pass1 == "1234" :
    jp_chase.if_you_are_auth_user(True,amount=your_amt)
else:
    jp_chase.if_you_are_auth_user(False,amount=your_amt)

#SUCCESS
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0131.py
# Enter your PIN to see your balance1234
# your balance is 500
# Enter your PIN to withdraw1234
# Enter the amount to withdraw200
# your balance is 500
# After withdrawal
# your balance is 300

# FAILURE
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0131.py
# Enter your PIN to see your balance12
# Not Allowed
# Enter your PIN to withdraw12
# Enter the amount to withdraw100
# Not Allowed
