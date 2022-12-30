# Matching randomly generted number

from random import randint

x = randint(0, 300)
x
digit = int(input("Please input a number between 0~300:"))
if digit == x:
    print('Bingo!')
elif digit > x:
    print('Too big!')
else:
    print('Too small!')
    