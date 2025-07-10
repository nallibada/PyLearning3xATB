#Define the function to extract digits recursively
def number_to_list(n):
    if n == 0:
        return []
    return number_to_list(n // 10) + [n % 10]

# Define the number
n = 12322
# n=12321




# Convert number to list of integers
p = number_to_list(n)
print(type(p))
print(p)
#print(p[0])
d=p.__len__()
# print(d)
if d%2!=0 :
    print(d, "is odd number of digits")
    i=0
    j=1
    while i != (d-j):
        print ("Loop starts")
        print("i :" ,i,"d-j:",d-j,"i+j:",i+j,"d-2j:",d-2*j)
        print("p[i] :", p[i], "p[d-j]:", p[d - j], "p[i+j]:", p[i+j],"p[d-2j]:", p[d-2*j])
        if p[i] == p[d-j] and p[i+j] == p[d-2*j]:
            print("if")
            # print (p[i])
            # print(p[i+j])
            # print(p[d-2*j])
            print("next loop")
            print(n, "is a palindrome number")
        else:
            print(n, "is NOT a palindrome number")
        i += 1
        print("i:", i)
        j += 1
        print("j:", j)

else :
    print (d,"is even number of digits")




