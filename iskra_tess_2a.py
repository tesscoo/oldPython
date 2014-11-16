#This program converts the user's temperature from Fahrenheit to Celsius

print('Hello, user!')

temp_f = int(input('What is the temperature in degrees Fahrenheit? '))

temp= ((temp_f)-32)*(5/9)
formatted_temp = format(temp, '.1f') #Cut off all the decimal places

print('If the temperature is ' + str(temp_f) + ' in degrees Fahrenheit,\n' + 'then it is ' + str(formatted_temp) + ' in degrees Celsius.') 

#Convert integer values to strings in order to add them to a statement.

