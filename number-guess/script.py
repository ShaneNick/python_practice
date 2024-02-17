import random 

print('Guess the number')

number = random.randint(1, 10)

input('What is your guess: ')

if input == number:
    print('Correct! You guessed correctly')
else:
    print(f"Wrong, the number was {number} try again")