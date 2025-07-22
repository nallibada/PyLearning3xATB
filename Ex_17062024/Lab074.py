numbers=[1,2,3]

def do_something(numbers):
    numbers.append(200)
    numbers[0]=56
    numbers[1] = 44
    numbers[2] = 22
    numbers[-1] = -11
    return numbers
l=do_something(numbers)
print ("Hello")
print(l)
