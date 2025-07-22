
# usage of lambda expression example - lambda expression is suitable for 1 liners, it is not suitable for multi liners.
def sum_two(a,b):
    s=a+b
    return s
l=sum_two(a=3,b=4)
print("The sum l is:",l,"\nThe sum of 2 no s a,b is:",sum_two(3,6))

o_f=lambda a,b:a+b
print("The sum o_f is:", o_f(7,5))

o_f1=lambda a,b,c:a-b-c
print("The subtraction o_f1 is:",o_f1(8,4,9))