import random




numCheckBad = True
rRange = 0
answer = 0

print( "\nWelcome to Convert your decimal numbers to BINARY! \n")
print( "What is the number range you want to learn from?")

# 

while True:
    try:
        # needs to be a number
        rRange = int(input("\nEnter upper boundary of this range: ")) + 1
        break
    except (ValueError, TypeError):
        print("Oops!  That was no valid number.  Try again...")

while True:
    
    rNum= int(random.randrange( rRange ))

    print( "\nWhat is the binary of " + str(rNum) + " ?")

    while True:
        try:
            # given bin - convert to int
            answer =  int(input("Answer: "), 2)
            break
        # catches if anything except 0 or 1 was given
        except (ValueError, TypeError):
            print("Oops!  That was not Binary.  Try again...")

    
    if format( answer, 'b') == format( rNum, 'b') :

        print( "\nYou are right!" )
        print( "The answer is " + format( rNum, 'b') )
    else:
        print( "That's incorrect..." )
        print( "The answer is " + format( rNum, 'b') )


    print("\nAsk again? Type \"no\" to quit... Otherwise press ENTER")

    if input() == "no" :
        print("Bye bye!")
        quit()

