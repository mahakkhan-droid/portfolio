import random

number=random.randint(1,100)
attempts=0

print("====NUMBER GUESSING GAME====")
print("guess a number between 1 to 100")

while True:
    guess=int(input("enter your guess: "))
    attempts+=1

    if guess < number:
        print("too low! try again")

    elif guess > number :
        print("too high ! try again")

    else:
        print("congralulations ! you guessed it ")
        print("total attempts: ",attempts)
        break
