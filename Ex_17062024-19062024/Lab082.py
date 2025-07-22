# List=[1,2,3,4,5]
# print (List)
# for i in List :
#     new_list=i*2
#     print("The list is:",new_list)
#     nl=[]
#     nl.append(i*2)
#     print(nl)
# print(nl)

"""List=[1,2,3,4,5]
print (List)
dl=[]
for i in List :
    dl.append(i*2)
print(dl) """

# Online Python compiler (interpreter) to run Python online.
#Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run i
#num=[1,2,3,4,5]
#print(num)

def double_item(num):
   return num*2

#ss=double_item(num)
#print(ss)

#ml=list(map(double_item,num))
#print(ml)
my_list=[1,2,3,4,5]
print("using list , map functions on function and list :",list(map(double_item,my_list)))
print("Using list, map function and lambda in single line code: ",list(map(lambda num:num**2,[1,2,3,4,5,6])))

"""
1) Takes each item from the list
2) Executes function on it
3) Return same number of elements (list)
"""