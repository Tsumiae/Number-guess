import random

top_of_range = input("type a number: ")



if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Input a number greater than 0.")
        quit()

else:
    print("Input a number greater than 0.")
    quit()

rn = random.randint(0, top_of_range)
guesses = 0 

while True:
    guesses += 1
    user_guess = input("guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("type number next time.")
        continue
    
    if user_guess == rn:
        print("guessed right!!!")
        break
    else:
        if user_guess > rn:
            print("you where above the number")
        else:
            print("you where below the number")

print("it took you", guesses, "guesses to get it right")
    
    
