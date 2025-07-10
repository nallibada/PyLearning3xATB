#
#     #return x if x < y else y
# Python program to demonstrate nested ternary operator
# # Task 2.2 ) Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1= float(input("Enter the first number :"))
num2= float(input("Enter the second number :"))
#print("num1is equal to num2" if num1==num2 else "num1 is greater than num2" if num1>num2 else "num1is less than num2" )
print((num1,'is equal to',num2) if num1==num2 else (num1, "is greater than", num2) if num1>num2 else (num1,"is less than",num2))

#print(num1 ," is greater than", num2 if num1>num2 else num1," is less than",num2   if num1<num2 else if num1==num2 num1," is equal to",num2)
#print("no is greater" if num1>num2 else "no is lesser" if num1<num2  else num1==num2 "is equal to")) is greater")