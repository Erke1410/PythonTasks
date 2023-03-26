current_year = 2023
name = input("Enter your name: ")
age = int(input("Enter ypur age: "))
copy = int(input("How many copy: "))

future_year = current_year + (100 - age)
print(copy *"Your name is " + name)
print(copy *f"You will turn 100 years in {future_year}\n" )
