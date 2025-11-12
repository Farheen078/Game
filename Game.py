import random

print("Guess The Number")
a= random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == a:
    print("You guessed it right")
else:
    print(" Sorry, the correct number was ",a)
