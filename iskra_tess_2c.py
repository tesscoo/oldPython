#This is a program that simulates Mad Libs.

#Asks for 5 different words of different parts of speech to be inserted into a narrative.

print("Let's play Mad Libs!")

verb = input('Give me a verb.')
adj = input('Give me an adjective.')
adv = input('Give me an adverb.')
place = input('Give me a place.')
name = input('Give me a name.')
verb2 = input('Give me another verb.')

print('One day, ' + name + ' and Bill Clinton were on their way to the ' + place
      + '.' + ' After they had just learned to ' + verb + ' they decided to ' + adv + ' ' +
      verb2 + ', just because.' + name + ' felt ' + adj + ' and then decided to return home.')
       
