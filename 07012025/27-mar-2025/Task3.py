#Define the function to extract digits recursively
def number_to_list(n):
    if n == 0:
        return []
    return number_to_list(n // 10) + [n % 10]

# Define the number
n = 12345678900000

# Convert number to list of integers
res = number_to_list(n)

print(res)

