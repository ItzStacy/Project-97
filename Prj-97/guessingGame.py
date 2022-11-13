import random

print("Number Guessing Game")

#Generate a random number between 1-9
number=random.randint(1,9)

#Input given by user into input box. Here number of chances are 5
chances=0

print("Guess a number(between 1 and 9)")

#While loop to count the number of chances

while chances < 5:
    #Enter a number between 1-9
    guess=int(input("enter your guess="))

    if guess==number:
        print("Congratulation! You won")
        break
    elif guess < number:
        print("Your guess was too low:Guess a number higher than",guess)
    else:
        print("Your guess was too high:Guess a lower number than",guess)
    
    #Increase the value of chance by one
    chances += 1

    #Check whether the user correct the guess number
    if not chances < 5:
        print("You lose!!The number is",number)