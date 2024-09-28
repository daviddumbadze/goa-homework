# 1)

frui_list = ["apple","banana","pear"]

frui_list.append("orange")
print(frui_list)

# 2)

frui_list = ["apple","banana","pear", "orange"]

frui_list.remove("orange")
print(frui_list)

# 3)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in number_list:
    print(i)

# 4)

animals = []

for _ in range(3):
    animal = input("Please enter an animal: ")
    animals.append(animal)

print(animals)

# 5)

name_list = ["david", "elene", "mari", "zura"]

for name in name_list:
    print("Hello " + name + "!")

# 6)

colors = ["white","black", "yellow"]

colors.insert(0, "black")
print(colors)

# 7)

number_list = [1, 3, 4, 2, 8, 5, 9, 7, 10]
number_list.sort()
print(number_list)

# 8)

frui_list = ["apple","banana","pear", "orange"]
print(frui_list.index("banana"))

# 9)

frui_list = ["apple","banana","pear", "orange"]
print(frui_list[::-1])

# 10)

numbers_list = [5, 20 , 34, 8]
result = []

for i in numbers_list:
    result.append(i * 2)
print(result)

# 11)

frui_list = ["apple","banana","pear", "orange"]
print(frui_list)

# 12)

numbers_list = [5, 20 , 34, 8]
print(numbers_list[0])

# 13)

frui_list = ["apple","banana","pear", "orange"]
print(len(frui_list))