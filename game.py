import random

def number_game():
    game_running = True

    # generate a random number between 1-100
    random_number = random.randint(1, 100)


    while game_running:
        # ask the plyer for a guess
        answer = input("pick a number any number ")

        # make answer an integer
        try: 
            answer = int(answer)
        except:
            print("thats not a number")
            continue

        # if the guess is too high print you are too high
        # if its too low print you are too low 
        # if its correct = let them know and end the game

        if answer > random_number:
            print("you are too high")

        elif answer < random_number:
            print("you are too low")

        else:
            print("i dont like this game anymore :(")
            game_running = False

x = 1

while x == 1:
    menu_choice = input ("""do you want to:
      1: play number game
      q: or quit
""")
    if menu_choice == "1":
        number_game()
    elif menu_choice == "q":
        break
    





# clear screen when play
# display a high score
