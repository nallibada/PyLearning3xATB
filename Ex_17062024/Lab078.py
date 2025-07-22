# lambda arguments:expression
def even_odd(num):
    if num%2==0 :
        print("The number",num,"is even")
    else:
        print("The number",num,"is odd")
even_odd(2)
f_e_o= lambda num:print("The number",num,"is even") if num%2==0 else print("The number",num,"is odd")
f_e_o(4)

# ''''''C:\Users\User\AppData\Local\Programs\Python\Python312\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_17062024\Lab078.py
# The number 2 is even
# The number 4 is even
#
# Process finished with exit code 0 ''''''