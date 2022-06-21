import random
chances = 5
number = random.randint(1,9)

guess = int(input('guess a number --> '))

while chances > 0: 
    print(guess)
    if(guess > number):
        print("The number", guess, "is too high.")
        chances = chances - 1
        print("You have", chances, "left")
    if(guess < number):
        print("the number", guess, "is too low")
        chances = chances -1
        print("You have", chances, "left")
    if(guess == number): 
        print('!YOU WIN!!')
        break
    guess = int(input('guess a new number --> '))
if(chances == 0):
    print('You lose! Your number was...', number)


        
    