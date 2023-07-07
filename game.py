# generate a random number between 1-100
import random
random_number = random.randint(1, 100)
#print(random_number)

game_running = True


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

