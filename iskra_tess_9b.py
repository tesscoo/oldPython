#Current Weather in NYC

import urllib.request

opening_tag = '<temp_f>'
closing_tag = '</temp_f>'

def access():
    page = urllib.request.urlopen('http://w1.weather.gov/xml/current_obs/KNYC.xml')
    xml = page.read()
    return xml

def parse():
    xml = str(access())
    opening_tag_index = xml.find(opening_tag)
    closing_tag_index = xml.find(closing_tag)
    temp = xml[(opening_tag_index + len(opening_tag)):closing_tag_index] 
    return temp

def main():
    temp = parse()
    temp = float(temp)
    if temp >= 70.0:
        print("The weather is currently warm in New York City.")
    elif 70.0 > temp >= 50.0:
        print("The weather is currently nice in New York City.")
    elif temp < 50.0:
        print("The weather is currently chilly in New York City.")
    print('(It is ' + str(temp) + ' degrees Fahrenheit.)')
    
        
    
main ()
