from time import time


fruit_list = []

for item in range (0, 4):
    fruit = input("Fruit: ")
    fruit_list.append(fruit)

print()
print("*** THE FRUIT LIST ***")
print(fruit_list)
for item in fruit_list:
    print(item)