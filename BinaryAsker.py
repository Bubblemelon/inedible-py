import random




numCheckBad = True
rRange = 0
answer = 0

print( "\n Welcome to Convert your decimal numbers to BINARY! \n")
print( "What is the number range you want to learn from?")

while True:
    try:
        rRange = int(input("\nEnter upper boundary of this range: "))
        break
    except (ValueError, TypeError):
        print("Oops!  That was no valid number.  Try again...")

while True:
    
    rNum= int(random.randrange( rRange ))

    print( "\nWhat is the binary of " + str(rNum) + " ?")


    while True:
        try:
            answer =  bin( int( input("Answer: ") ) )[2:]
            break
        except (ValueError, TypeError):
            print("Oops!  That was not Binary.  Try again...")
    

    print( "The answer is " + format( rNum, 'b') )

    print("Ask again? Type no to quit... Otherwise press ENTER")

    if input() == "no" :
        print("Bye bye!")
        quit()

