import random
num=random.randint(1,12)

guess=int(input("Guess a number between 1 to 12 :-"))

while num!=guess:
    if num>guess:
        print(" You guessed too small...!")
    else:
        print("you guessed too large...!")
    guess = int(input("Guess a number:- "))
print("your guess is right,congratulation")
