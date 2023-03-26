import random

# num = random.randint(1,9)
# number_choose = int(input("Guess a number: "))
# while (number_choose != "exit"):
#     if num == number_choose:
#         print("You gussed it right!")
#         continue
#     elif num < number_choose:
#         print("Too high, sorry!!!")
#         continue
#     elif num > number_choose:
#         print("Too low, guess again")
#         continue
#     else:
#         print("Wrong input!!!")
# print(num)

# num = random.randint(1,9)
# guess = 0
# i = 0
# while guess != num and guess != "exit":
#     guess = input("Guess a number between 1 an 9: ")
#     if guess == "exit":
#         break
#     guess = int(guess)
#     i += 1
#     if guess < num:
#         print("Too low, guess again!")
#     elif guess >num:
#         print("Too high, guess again!")
#     else:
#         print("You guessed it!!!")
#         print("Took only ", i," tries! :)")
# input()

MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True

print("Alright...")

while RUNNING:
    GUESS = input("What is your lucky number? ")
    if int(GUESS) < NUMBER:
        print("Wrong, too low.")
    elif int(GUESS) > NUMBER:
        print("Wrong, too high.")
    elif GUESS.lower() == "exit":
        print("Better luck next time.")
    elif int(GUESS) == NUMBER:
        print("Yes, that's the one, %s." % str(NUMBER))
        if TRY < 2:
            print("Impressive, only %s tries." % str(TRY))
        elif 2 < TRY < 10:
            print("Pretty good, %s tries." % str(TRY))
        else:
            print("Bad, %s tries." % str(TRY))
        RUNNING = False
    TRY += 1
