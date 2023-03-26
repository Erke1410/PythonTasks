# import sys
#
# user1 = input("what is your name: ")
# user2 = input("what is your name: ")
# user1_choice = input("%s, do you want to choose rock, paper or scissors? " %user1).lower()
# user2_choice = input("%s, do you want to choose rock, paper or scissors? " %user2).lower()
#
# def game(first_choice, second_choice):
#     if first_choice == second_choice:
#         return("It's a tie!")
#     elif first_choice == "rock":
#         if second_choice == 'scissors':
#             return ("Rock wins!")
#         else:
#             return ("Paper wins!")
#     elif first_choice == "scissors":
#         if second_choice == "rock":
#             return ("Rock wins!")
#         else:
#             return ("Scissors wins!")
#     elif first_choice == ("paper"):
#         if second_choice == "rock":
#             return ("Paper wins")
#         else:
#             return ("Scissors wins!")
#     else:
#         return ("Invalid input! Enter correct input. Try again!")
#     sys.exit()
#
# print(game(user1_choice, user2_choice))

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')