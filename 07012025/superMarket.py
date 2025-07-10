from datetime import datetime

# name = input("Enter your name:")
# lists = '''
# Rice     Rs 20/kg
# Sugar   Rs 30/kg
# Salt      Rs 20/kg
# Oil        Rs 80/kg
# Paneer  Rs 110/kg
# Maggi   Rs 50/kg
# Boost    Rs 90/kg
# Colgate Rs 85/kg
# '''
# print(lists)

item = {'Rice': 20, 'Sugar': 30, 'Salt': 20, 'Oil': 80, 'Paneer': 110, 'Maggi': 50, 'Boost': 90, 'Colgate': 85}
option = int(input("Enter 1 to shop and 2 for exit:"))
if option == 2:
    print("don't shop")
elif option == 1:
    shop_cart= input("Enter your items:")
    for i in range(1, item.__len__(), 1):
        print("elif")


