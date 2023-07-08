import random

def number_game():
    random_number = random.randint(1, 100)
    print (random_number)
    guess = input("""pick a number any number (between 1-100)
""")
    guess = int(guess) 
    if guess > random_number:
        print("your guess is too high")
    elif guess < random_number:
        print("your guess too low")

number_game()

# game_main_menue = input ("""do you want to play a game?:
#     1: number game
#     q: quit
# """)
# if game_main_menue == "1":
#     number_game()

#elif game_main_menue == "q":
    #break

