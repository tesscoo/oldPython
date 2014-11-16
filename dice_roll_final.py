import random
def dice_roll():
    '''Rolls dice for the user.'''
    rolls= []
    for roll in range(100):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        rolls.append((roll1,roll2))
    return rolls

def main():
    '''Gvies average of 100 dice roll.'''

    ans=0.0
    rolls = dice_roll()
    for roll in rolls:
        ans = sum(roll) + ans

    average = ans/100

    print('The average of all the rolls is ' + str(average))

main()
