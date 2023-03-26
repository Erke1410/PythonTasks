number1 = int(input("Enter Number: "))
number2 = int(input("Enter divide by number: "))
if number1 != number2:
    if number1 % 2 == 0:
        print(f"{number1} is even number")
        if number1 % 4 == 0:
            print(f"{number1} is even and can be divided by 4")
    else:
        print(f"{number1} is odd number")
    number3 = number1 / number2
    print(f"{number1} / {number2} is {number3}")
elif number1 == number2:
    print(f"Number A ({number1}) and number B ({number2}) are the same!")
