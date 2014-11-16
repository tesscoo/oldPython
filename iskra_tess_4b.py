#Fibonacci Sequence Generator
#This program uses a while-loop

n = int(input('How many Fibonacci sequence entries would you like to generate? '))

i=1

x=0 #Assignment of first given Fibonacci numbers
y=1
z=1

while i < n+1:# If I only say i < n, the program gives me one less than the user asks for, i.e. gives 9 numbers instead of 10
    print(str(x))
    i=i+1
    if i>1:
        z=x+y #Reassignment once the first given numbers have passed
        x=y
        y=z

print('Done!')

