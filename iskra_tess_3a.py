#This program simulates the functionality of a Magic 8 Ball.

import random

ques = input('Ask me a yes or no question. ')

ball = random.randint(1,5)

if ball == 1:
    print('Certainly!')
elif ball == 2:
    print("I'm not sure.")
elif ball == 3:
    print('Maybe.')
elif ball == 4:
    print("I don't think so.")
elif ball == 5:
    print('Definitely no.')

print('Thanks for playing!')


