# Leap Year Checker
## Create a program that determines whether a given year is a leap year
# A leap year is divisible by 4 , but not by 100 unless it is also  divisible by 400. Use an if-else statement to make this determination.
# input=2024
# output=Leap year

""""How to Determine Whether Any Year is a Leap Year?
To determine whether any given year is a leap year, follow these steps:
If the year is evenly divisible by four, then go to step 2. Otherwise, go to step 5.
If the year is evenly divisible by a hundred, then go to step 3. Otherwise, go to step 4.
 If the year is evenly divisible by four hundred, then go to step 4. Otherwise, you can go to step 5.
The year is a leap year (if it has 366 days).
The year is not a leap year (if it has 365 days).
"""
ly = int(input("Enter the  year:"))
if ly%4==0 :
    if  ly % 100 ==0 :
        if ly%400==0  :
            print(ly, "is leap year")
        else:
            print(ly, "is not leap year")
    else:
        print(ly, "is leap year")
else :
    print(ly,"is not a leap year")
