#Fibonacci Sequence Generator
#This program uses a main function

def main():  
    n = int(input('How many Fibonacci sequence entries would you like to generate? '))

    i=1

    x=0 
    y=1
    z=1

    while i < n+1:
        print(str(x))
        i=i+1
        if i>1:
            z=x+y
            x=y
            y=z

    print('Done!')


    
main()
