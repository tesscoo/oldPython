#Average Exam Score Generator
#This program uses a for-loop

total = 0

for i in range(12):
    score = input('Enter exam score ' + str(i+1) + ' : ')
    total = total + int(score)

average = total//12 #This will chop of the decimal point

print('The average exam score is ' + str(average) + ' .')
