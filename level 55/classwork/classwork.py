
ice_cream_flavors = {
    "შოკოლადი": "delicious",
    "ვანილი": "sweet",
    
}


flavor_to_check = input("შეიყვანე ნაყის სახელი: ")

if flavor_to_check in ice_cream_flavors:
    print("ყოჩაააღღღ !!!")
else:
    print("არასწორია ნო ნო !")