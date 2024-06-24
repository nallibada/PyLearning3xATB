#
#     #return x if x < y else y
#
# # Task 2.2 ) Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
# num1= float(input("Enter the first number :"))
# num2= float(input("Enter the second number :"))
#
# #print(num1,"is equal to", num2 if num1==num2 else "num1 is not equal to num2")
# #print(num1 ," is greater than", num2 if num1>num2 else num1," is less than",num2   if num1<num2 else if num1==num2 num1," is equal to",num2)
# print("no is greater" if num1>num2 else ("no is lesser" if num1<num2  else num1==num2 "is equal to"))
#
# # Python program to demonstrate nested ternary operator
a = 10
b = 20

print("Both are equal" if a == b else "a is greater"
      if a > b else "b is greater")