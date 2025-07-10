class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def show_balance(self):
        print ("your balance is", self.balance)

jp_chase = BankAccount()
print(jp_chase.balance)
jp_chase.deposit(101)
jp_chase.show_balance()
jp_chase.withdraw(99)
jp_chase.show_balance()

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0130.py
# 0
# your balance is 101
# your balance is 2
#
# Process finished with exit code 0