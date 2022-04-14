import random

def numberGuess():
  random_num = random.randint(1,10)
  guess = int(input("Guess a number between 1 and 10: "))
  
  while True:
    if (guess == random_num):
        print ("You got it!")
        break
    if (guess > random_num):
        print ("Wrong! Your guess is too high")
        guess = int(input("Guess another number: "))  
      
    if (guess < random_num):
        print ("Wrong! Your guess is too low")
        guess = int(input("Guess another number: "))

    #if (numberGuess == "Y" or numberGuess == "y" or numberGuess == "yes" or numberGuess == "Yes"):
      
numberGuess ()