class password:
    def __init__(self,password):
        self.__password=password
        self.public_var=10

    def get_password(self, is_auth):
        if is_auth :
            print("The initial password set is :",self.__password)

        else:
            print("invalid password")

    def set_password(self, password):
        if len(password)>10 :
            self.__password=password
            print("The new password set is : ",self.__password)
        else:
            print("Not allowed , weak password")

pwd=password("Neelima123")
#pwd.get_password(False)
pwd.get_password(True)
chg_pwd=input("Enter the new password:")
pwd.set_password(chg_pwd)
#pwd.set_password("test123")

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0132.py
# The initial password set is : Neelima123
# The new password set is :  dfdjskfkljdflkdjflds

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0132.py
# The initial password set is : Neelima123
# Not allowed , weak password

# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0132.py
# The initial password set is : Neelima123
# Enter the new password:1dfsafaf
# Not allowed , weak password


# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_28062024\Lab0132.py
# The initial password set is : Neelima123
# Enter the new password:gfgfdgfdgfdgfdg
# The new password set is :  gfgfdgfdgfdgfdg
