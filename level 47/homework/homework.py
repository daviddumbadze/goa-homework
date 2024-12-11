import random 
def random_movies():
    list =["interstelar", "შერეკილები"] 
    list_of_random_movies =["ქათმები", "მამლები", "ჩხიკვთა ქორწილი", "home alone ","elephant story","შრეკიი"]#ეს არის ის სია რომელი სიიდანაც ელემენტი გამოვა ორიგინალშიი
    for i in range(4):# ეს არის for loop for loop ით გადავუვლით ამ სიას და დავამატებთ list_of_random_movies-იდანნ
        random_item = random.choice(list_of_random_movies)#ეს random ფილმს აირჩევს 
        list.append(random_item)#ეს ჩაამატებს ორიგინალში list_of_random_movies-ის ელემენტს
        list_of_random_movies.remove(random_item)#ეს წაშლის ზედმეტს
        return list #ეს ლისტ იძახებს
    print(random_movies())