#1
number = int(input("Please enter a number: "))

if number == 0:
    print("Number is 0")
elif number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# 2)

num1 = int(input("Please enter a firs number: "))
num2 = int(input("Please enter a second number: "))

if num1 > num2:
    print(num1, ">" , num2)
elif num1 < num2:
    print(num1, "<" , num2)
else:
    print(num1, "=", num2)

number = int(input("Please enter a number in range 1-10: "))

if number == 6:
    print("You win 100.000$")
elif number == 2:
    print("You win 10.000$")
else:
    print("You win 10$")