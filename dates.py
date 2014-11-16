#How many days are in between two dates

date_1_mo = input('What is the month of the first date? ')
date_1_day= input('What is the day of the first date? ')
date_2_mo = input('What is the month of the second date? ')
date_2_day = input('What is the day of the second date? ')

#Converting the date to a number of the year

if date_1_mo == 'January':
    x = 0
elif date_1_mo == 'February':
    x = 31
elif date_1_mo == 'March':
    x = 59
elif date_1_mo == 'April':
    x = 90
elif date_1_mo == 'May':
    x = 121
elif date_1_mo == 'June':
    x = 151
elif date_1_mo == 'July':
    x = 182
elif date_1_mo == 'August':
    x = 213
elif date_1_mo == 'September':
    x = 244
elif date_1_mo == 'October':
    x = 274
elif date_1_mo == 'November':
    x = 305
elif date_1_mo == 'December':
    x = 335
else:
    print('Please enter a valid month.')

y= int(date_1_day)

if date_2_mo == 'January':
    m = 0
elif date_2_mo == 'February':
    m = 31
elif date_2_mo == 'March':
    m = 59
elif date_2_mo == 'April':
    m = 90
elif date_2_mo == 'May':
    m = 121
elif date_2_mo == 'June':
    m = 151
elif date_2_mo == 'July':
    m = 182
elif date_2_mo == 'August':
    m = 213
elif date_2_mo == 'September':
    m = 244
elif date_2_mo == 'October':
    m = 274
elif date_2_mo == 'November':
    m = 305
elif date_2_mo == 'December':
    m = 335
else:
    print('Please enter a valid month.')

n = int(date_2_day)

day1= x+y
day2= m+n

difference = day2 - day1

print('There are ' + str(difference) + ' days between your dates.')
