import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess < num:
        print("Guess is too low!")
    elif guess > num:
        print ("Guess is too high!")
    if guess == num:
        print("Congratulations, you got it!")
        #play = input("Would you like to play again? (Y) or (N): ")
      
    #if play == ("Y" or play == "y" or play == "yes" or play == "Yes"):
      #play_game()