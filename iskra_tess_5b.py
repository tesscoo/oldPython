#If it were not for the assignment, I would call this something like time.py
#Time Conversion Module

'''Converts given time to seconds, minutes, or hours
based on a given number of days.'''

# To use the module, we would have to import it first
# import time


def seconds(day=1): #default parameter of 1 day
    '''Converts number of days to seconds.'''
    print('This is ' , day * 86400 , ' seconds.')

def minutes(day=1):
    '''Converts number of days to minutes.'''
    print('This is ' , day * 1440 , ' minutes.')

def hours(day=1):
    '''Converts number of days to hours.'''
    print('This is ' , day * 24 , ' hours.')

    
