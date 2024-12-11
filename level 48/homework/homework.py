import random

def add_random_numbers_to_list(input_list):
    return [x + random.randint(1, 50) for x in input_list]


my_list = [10, 20, 30, 40, 50]
new_list = add_random_numbers_to_list(my_list)
print(new_list)
