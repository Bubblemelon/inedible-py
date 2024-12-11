import random, time, sys

numCheckBad = True
rRange = 0
answer = 0
tFastest = sys.maxsize
tFastestMsg = ""

print( "\nWelcome to Convert your decimal numbers to BINARY! \n")
print( "What is the number range you want to learn from?")

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

    # see current Epoch Time
    # https://www.epochconverter.com/
    t0 = time.time()

    while True:
        try:
            # given bin - convert to int
            answer =  int(input("Answer: "), 2)
            break
        # catches if anything except 0 or 1 was given
        except (ValueError, TypeError):
            print("\nOops!  That was not Binary.  Try again...")


    if format( answer, 'b') == format( rNum, 'b') :
        print( "\nYou are right!" )

    else:
        print( "\nThat's incorrect..." )

    print( "\nThe answer is " + format( rNum, 'b') + "." )

    t1 = time.time()
    tDiff = t1 - t0
    # total milliseconds taken
    milliseconds = int(round(tDiff * 1000))

    timeMessage = "%dm %ds %sms" % (int(tDiff/60) , int(tDiff%60), milliseconds%1000)

    if tFastest > tDiff :
        tFastest = tDiff
        tFastestMsg = timeMessage

    print("\nTime taken = " + timeMessage )

    print("\nAsk again? \nType \"no\" exactly to quit...\nOtherwise" +
        " press ENTER or type anything to continue.")

    if input() == "no" :
        print("\nWow! Your fastest time is " + tFastestMsg + " <---")
        print("\nBye bye =)")
        quit()