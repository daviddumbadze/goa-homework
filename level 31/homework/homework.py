my_list = [1, "ტექსტი", 3.14, True, None, "მომხმარებელი", 42, [1, 2, 3], (4, 5), {'key': 'value'}]
new_element = input("რა მონაცემის დამატება გსურთ სიაში? ")
index = int(input("რომელ ინდექსზე გსურთ დამატება (0-დან 10-მდე)? "))
my_list.insert(index, new_element)
