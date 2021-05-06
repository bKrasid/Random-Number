import random

guesses = 5
number = random.randint(0,100)
answer = 0

while (guesses != answer and guesses):
    answer = int(input("Guess the  number! "))
    guesses -= 1
    if (answer > number):
        print("Lower the number of guesses." + str(guesses))
    elif (answer < number):
        print("Higher the number of guesses." + str(guesses))
    elif (answer == number):
        print("Correct! You guessed the number!" + str(guesses))
if(answer != number):
    print("Sorry, but you didnot guess the number. The number was: " + str(number))
