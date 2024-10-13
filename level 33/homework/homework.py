#1
names = "ლუკა გიო ნინო ნიკა ლიზი"
names_list = names.split()
for name in names_list:
    print(f"გამარჯობა {name}")
#2
names = ["ლუკა", "გიო", "ნინო", "ნიკა", "ლიზი"]
capital_names = [name.upper() for name in name]
print(capital_names)
