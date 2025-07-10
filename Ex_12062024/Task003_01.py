"""2. Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input = side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
"""
s1= float(input("Enter the s1 of traingle:"))
s2= float(input("Enter the s2 sides of traingle:"))
s3= float(input("Enter the s3 sides of traingle:"))

if s1==s2==s3 :
    print("Equalateral triangle")
elif s1 == s2 != s3 or s1 != s2 == s3 or s1 == s3 != s2 :
    print( "isoceles triangle")
else :
    print("scalene triangle")
