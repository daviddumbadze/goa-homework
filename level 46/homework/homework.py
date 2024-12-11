import random

def choose_random_item():
 
    items = ['ლომი(ბატონი დავითი)', 'ვეფხვი', 'მგელი', 'ტურა', 'დათვი']
    
   
    selected_item = random.choice(items)
    
    return selected_item


print(choose_random_item())
