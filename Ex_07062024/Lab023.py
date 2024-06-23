# List -Data Type
#List -Shopping list
#milk, bread,butter, poha

#1. add item,
#2. remove item
#3. Update item
#4. View item
#5. Exit

shopping_list=["milk","butter","bread","poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])


# add item to list
shopping_list.append("curd") #add item in the list
print(shopping_list)
# my_list=[1,2,3,4,True,3.14,'Pramod']
# print(type(my_list)) #<class 'list']

shopping_list.insert(1,"pizza") # add item in the list at specific position
print(shopping_list)

shopping_list.extend(['chips',"coca cola","maggi noodles"]) # add multiple items in the list at the end
print(shopping_list)

shopping_list.remove("butter") # remove item from the list
print("REMOVE item from the list: butter")
print(shopping_list)
##########################################################################
#Remove the last item from the list :pop function is used
#shopping_list.pop(1) - when we use index in the pop that item will be deleted from list and without any index , by default it deletes last item in the list for which the index is -1
shopping_list.pop()
print("POP: deletes last item")
print(shopping_list)
# to do reverse of the list
shopping_list.reverse()
print (shopping_list)
#sort of list
shopping_list.sort()
print (shopping_list)
#it is mutable sequence, we can change the value
shopping_list[3]="coke"
print(shopping_list)

#to find the index of any item in the list
print(shopping_list.index("pizza"))


# RESULT::
# C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_07062024\Lab023.py
# ['milk', 'butter', 'bread', 'poha']
# 4
# milk
# poha
# ['milk', 'butter', 'bread', 'poha', 'curd']
# ['milk', 'pizza', 'butter', 'bread', 'poha', 'curd']
# ['milk', 'pizza', 'butter', 'bread', 'poha', 'curd', 'chips', 'coca cola', 'maggi noodles']
# REMOVE item from the list: butter
# ['milk', 'pizza', 'bread', 'poha', 'curd', 'chips', 'coca cola', 'maggi noodles']
# POP: deletes last item
# ['milk', 'pizza', 'bread', 'poha', 'curd', 'chips', 'coca cola']
# ['coca cola', 'chips', 'curd', 'poha', 'bread', 'pizza', 'milk']
# ['bread', 'chips', 'coca cola', 'curd', 'milk', 'pizza', 'poha']
# ['bread', 'chips', 'coca cola', 'coke', 'milk', 'pizza', 'poha']
# 5