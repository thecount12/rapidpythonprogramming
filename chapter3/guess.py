#!/usr/bin/python
# guess.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming


number = 10
guess = int(raw_input('Enter an integer between 1 and 20: '))
if guess == number:
        print 'Congratulations! Correct number is', number 
elif guess < number:
        print 'No, try a little higher'
else:
        print 'No, try a little lower'

