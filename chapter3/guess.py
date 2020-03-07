"""
guess.py
Chapter 3 input
Author: William C. Gunnells
Rapid Python Programming
"""


number = 10
guess = int(input('Enter integer 1 through 20: '))
if guess == number:
    print('Congrats! Correct number is', number)
elif guess < number:
    print('No, try a little higher')
else:
    print('No, try a little lower')

