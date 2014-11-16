#This program encrypts messages for the user.

def change(character):
    '''Encodes the characters of the user's string.'''
    encoded_character = 3 * ord(character)
    return encoded_character
        

def main():
    '''Encrypts the user's message.'''

    message = input('Please enter the message you would like to encrypt: ')
    
    for character in message:
        encoded_character = change(character)
        print(encoded_character, end=' ')


main()

    

        
