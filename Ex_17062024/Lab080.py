# List - collection of items (Duplicate is allowed)
my_list=[1,2,3]
#my_list2=[1,True,"Pramod", 12.34]
#indexing
print("Element at index[0]:",my_list[0])
#changing the element
my_list[1]=20
print("List after changing the element at index[1]:", my_list)

#appending the element
my_list.append(99)
print("List after appending the element:", my_list)

#extend the list
my_list.extend([5])
print("List after extending:", my_list)

#remove the list
my_list.remove(20)
print("List after removing:", my_list)

# MY COPY LIST
MY_COPY_LIST=my_list.copy()
print ("Original list before copying", my_list)
print ("list after copying", MY_COPY_LIST)
my_list.clear()
#print ("List after clearing", my_list)
#print ("index[3] of list", my_list[3])
MY_COPY_LIST.reverse()
print(MY_COPY_LIST)
MY_COPY_LIST.sort()
print(MY_COPY_LIST)
print(MY_COPY_LIST[0])
print(MY_COPY_LIST[1])
print(MY_COPY_LIST[2])
print(MY_COPY_LIST[3])



# '"'' C:\Users\User\AppData\Local\Programs\Python\Python312\python.exe C:\Users\User\PycharmProjects\PythonTesting\PyLearning3xATB\Ex_17062024\Lab080.py
# Element at index[0]: 1
# List after changing the element at index[1]: [1, 20, 3]
# List after appending the element: [1, 20, 3, 99]
# List after extending: [1, 20, 3, 99, 5]
# List after removing: [1, 3, 99, 5]
# Process finished with exit code 0 """