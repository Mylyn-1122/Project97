import random

number = random.randrange(1, 9)
chances = 5

while chances >= 1:
    guess = int(input("Please Guess a Number Between 1 and 9: "))

    if (guess == number):
        print("You Win!")
        break
    elif (guess < number):
        print('Your guess is too low')
        chances = chances -1
        
    else:
        print('Your guess is too high')
        chances = chances -1

if(chances == 0):
    print('you lost the number is ', number)

