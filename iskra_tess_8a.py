#This program encrypts and decrypts messages for the user using lists.

def change(character):
    '''Encodes the characters of the user's string.'''
    encoded_character = 3 * ord(character)
    return encoded_character
        

def encoder(message):
    '''Encrypts the user's message.'''

    list = []
    
    for character in message:
        encoded_character = change(character)
        list.append(encoded_character)
    return(list)

def decoder(list):
    '''Decodes the user's list.'''
    decoded_str = ''
    for encoded in list:
        decodedValue = int(encoded/3)
        decoded_char = chr(decodedValue)
        decoded_str += decoded_char
    return decoded_str




#For example, input decoder(encoder('Hello'))
#This returns 'Hello'
    
