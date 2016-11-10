from random import randint

roundOver = False #keep track of whether the game is active or not
houseWins = False #did the house win the round
playerWins = False #did the player win the round
pointOn = False #is the point set
playerBank = 10000 #start with $10,000
betAmount = 0

name = raw_input("\nHello, what is your name? ")
print "Hi " + name + ", welcome to the DigitalCrafts Casino.  Let's play some craps!"
#roll() function
def roll():
    global pointOn #let me see if the point is on within this function
    global point #let us keep track of the point from within this function
    global roundOver,houseWins,playerWins #access win flags from within the roll

    if not(pointOn):
        #accept pass line bets only on first roll
        wager()

    #roll dice
    d1 = randint(1,6)  #get random number between 1 and 6
    d2 = randint(1,6)  #get random number between 1 and 6

    value = d1+d2 #what the player rolled
    print "Player rolls a: " + str(value) #must convert the value to a string

    if pointOn:
        if point==value: #player matched the point
            print "Player hit the point, player wins"
            roundOver = True
            houseWins = False
            playerWins = True
        elif value==7:
            print "Player rolled a 7, house wins"
            roundOver = True
            houseWins = True
            playerWins = False
    else :
        if value==2 or value==3 or value==12:
            houseWins=True
            playerWins=False
            roundOver=True
            print "Player crapped out, house wins"
        elif value==7 or value==11:
            houseWins=False
            playerWins=True
            roundOver=True
            print "Player rolled a 7 or 11, player wins"
        else:
            #the point isn't on set it
            point=value #set the point to the player's roll
            pointOn = True #turn this on so we only set it if not already set
            print "The point is on and set to: " + str(point)

#End of roll() function

def startGame():
    global roundOver,point,pointOn,betAmount,playerBank
    #reset the starting point
    point=0
    roundOver=False
    pointOn=False

    #roll until the game ends
    while not roundOver:
        roll()

    #adjust the player bank
    if houseWins:
        playerBank = playerBank - betAmount
    elif playerWins:
        playerBank = playerBank + betAmount

    print "\nYou now have $"+str(playerBank)

    #after the round ends, prompt to restart
    inp = raw_input("\nEnter 'r' to roll or any other key to exit the game:   ")
    if inp.lower()=='r':
        startGame()
    else:
        print "\nGame Over"

def wager():
    global playerBank,betAmount
    #\n are new line characters
    print "\n"
    print "You have $" + str(playerBank)
    print "\n"

    betAmount = raw_input("How much would you like to bet? ")
    #betAmount is a string, we need to covert it to an integer (or float)
    betAmount = int(betAmount)

    if betAmount>playerBank:
        print "Please enter a smaller wager"
        wager()

    #if the bet is less than zero, they would cheat by playing with the house
    if betAmount<0:
        print "Please enter a number >= 0"
        wager()

#start the game
startGame()
