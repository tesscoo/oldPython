#This program gives the user their horoscope.
#The user gives their astrological sign first.

bday = input('''I will give you your horoscope if you wish...
What is your birthday? Use the form mmdd: ''')
bday = int(bday)

if bday >= 1222 or bday <= 120:
    print('''Capricorn: Be sure to bundle up this month because some
of your friends are going to get icy.''')
elif 121 <= bday <= 219:
    print('''Aquarius: You're going to slide into money this month: Watch out!''')
elif 220 <= bday <= 320:
    print('''Pisces: Try to have some adventure in your life this month.''')
elif 321 <= bday <= 420:
    print('Aries: Study hard for your big exam!')
elif 421 <= bday <= 521:
    print('''Taurus: Take the trip that you've been wanting to go on this month.''')
elif 522 <= bday <= 621:
    print('Gemini: Invest your money in something new. It will pay you back nicely.')
elif 622 <= bday <= 722:
    print('Cancer: You will meet new friends soon, so be open and stay smiling.')
elif 723 <= bday <= 822:
    print('Leo: Stay in with your significant other this weekend and your relationship will benefit.')
elif 823 <= bday <= 923:
    print('Virgo: Stay calm when trouble is brewing, and your friends will always come to you.')
elif 924 <= bday <= 1023:
    print('Libra: When you make new friends, you heart will benefit. Get out there!')
elif 1024 <= bday <= 1122:
    print('Scorpio: Study hard and your grades will rise. The corners of your mouth will follow!')
elif 1123 <= bday <= 1221:
    print('Sagittarius: Get good sleep tonight, for something is in store for you later this week.')



