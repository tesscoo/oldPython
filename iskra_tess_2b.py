#This program simulates rolling a pair of dice and adding the two values that appear.

import random #Modules should be shown at the beginning

dice_one = random.randint(1, 6)
dice_two = random.randint(1, 6)

print('Roll your dice!')

print('The results are ' + str(dice_one) + ' and ' + str(dice_two))

total = dice_one + dice_two

print('Your roll totals ' + str(total))
