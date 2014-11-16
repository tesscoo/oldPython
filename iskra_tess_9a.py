#Searches Shakespeare's Sonnets for a user defined word or phrase
#Writes these lines to a new text file

search_term = input('What word or phrase art thou searching for? ')

file_write = open('yourlines.txt', 'w')
file_parse = open('sonnets.txt', 'r') #Works when sonnets.txt is in my cwd 

line_count = 0

for line in file_parse:
    if search_term.lower() in line.lower(): #Catches all occurrences 
        line_count = line_count + 1
        file_write.write(line)

print('Found ' + str(line_count) + ' occurrences of ' + search_term) #For fun
        
