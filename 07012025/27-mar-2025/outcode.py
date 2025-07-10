n=123456789100000000
number_to_list = n // 10
nl=n % 10
print(number_to_list)
print(nl)
print(number_to_list,nl)


# Define the function to extract digits recursively
# def number_to_list(n):
#     if n == 0:
#         return []
#     return number_to_list(n // 10) + [n % 10]
#
# # Define the number
# n = 12345
#
# # Convert number to list of integers
# res = number_to_list(n)
#
# print(res)

 # Find whether given number is palandrome number or not '

# pl = input("Enter the num:")
#
# # Define the number
# #n = 12345
#
# # Convert number to list of integers
# res = list(map(int, str(pl)))
#
# print(res)
# # neel= pl.split()
# #n=neel.split()
# print(type(neel))
# print(neel)
# print(neel[0][0])
# d1=neel[[0][0]]
# d2=neel[[0][1]]
# d3=neel[[0][2]]

# print(d1,d2,d3)
#print(n)
# for i in Range(3)
# if num1 == num2 :
#     print(num1, "is equal to ",num2)
#
# elif  num1 > num2 :
#     print(num1, "is greater than ", num2)
#
# elif  num1 < num2 :
#     print(num1, "is lesser than ", num2)
#################################################

#Define the function to extract digits recursively
def number_to_list(n):
    if n == 0:
        return []
    return number_to_list(n // 10) + [n % 10]

# Define the number
n = 12321

# Convert number to list of integers
p = number_to_list(n)
print(type(p))
print(p)
print(p[0])
d=p.__len__()
# print(d)
i=0
j=1
while i != (d-j):
    print ("loop")
    print("i :" ,i,"d-j:",d-j,"i+j:",i+j)
    print("p[i] :", p[i], "p[d-j]:", p[d - j], "p[i+j]:", p[i+j])
    if p[i] == p[d-j] and p[i+j] == p[d-j]:
        print("if")
        print (p[i])
        print(p[i+j])
        print(p[d-j])
        print("next loop")
    else :
        print("else")
    i += 1
    print("i:",i)
    j += 1
    print("j:",j)

