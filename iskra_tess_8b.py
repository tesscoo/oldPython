# This program will establish a grocery list with prices and return whatever
# the user requests.

grocery_list = {'glass slipper': 20, 'crown': 100, 'ballgown': 200,
                'earrings': 15, 'carriage': 1000, 'makeup': 10}

def main():
    '''Allows user to access the grocery list based on an input statement.'''
    
    selection = input('''Enter 'inventory' to see all items or enter a specific itemto see its price. ''')

    if selection == 'inventory':
        for item in grocery_list:
            print(item)
    elif selection == 'glass slipper':
        print('The cost of the item is $', grocery_list.get('glass slipper'), '.')
    elif selection == 'crown':
        print('The cost of the item is $', grocery_list.get('crown'), '.')
    elif selection == 'ballgown':
        print('The cost of the item is $', grocery_list.get('ballgown'), '.')
    elif selection == 'earrings':
        print('The cost of the item is $', grocery_list.get('earrings'), '.')
    elif selection == 'carriage':
        print('The cost of the item is $', grocery_list.get('carriage'), '.')
    elif selection == 'makeup':
        print('The cost of the item is $', grocery_list.get('makeup'), '.')
    else:
        print('Please enter a valid selection.')
    
main()
