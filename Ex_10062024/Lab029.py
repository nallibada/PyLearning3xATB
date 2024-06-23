#Operators
#1. Unary Operator
#2. Binary Operator
#3. Ternary Operator

#1. Unary Operator
#It has a single operand
a=10
n = 7
print(-n)  # Prints: -7
flag = True
print(not flag)  # Prints: False
    #1.1 Unary operator +
a=5
print(a) #Prints: -5
#1.2 Unary Operator -
b=10
print(-b) #Prints: -10
#1.3 Logical negation operator not
c=5
print(c) #Prints: False
print(not c) #Prints: False
#1.4 bitwise    operator ~
d=5
print(~d) #Prints: -6
#1.5 identity operator is, is not
e=3
f=3
print (e is f) #Prints: True
print (e is not f)
if  e is f:
    print("e and f are same") #Prints: e and f are same
    list1= [1,2,3]
    list2= [1,2,3]
    print(list1 is list2) #Prints: False
    print(list1 is not list2) #Prints: True

#Binary operators operate on two operands. Common examples include arithmetic operators like +, -, *, /, and logical operators like and, or
#Arithematic Operators : +, -, *, /, //, %, **
a=90
b=10
print(a+b) #Prints: 100
print(a-b) #Prints: 80
print(a*b) #Prints: 900
print(a/b)
print(a%b) #Prints: 10
print(87%10) # - Modulus -remainder
print(87//10)#- Quotient
print(2**3) #Prints: 8