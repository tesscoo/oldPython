#This program returns the URL associated with a user's email address

def main():
    '''Returns the URL associated with a user's email address.'''

    user = input('Please enter your full email address: ')

    index = user.find('@')

    url_1 = user[0:index+1] #Splits the string

    url_2 = user[index+1:len(user)]
    

    print('http://www.'+url_2)

main()
