from time import sleep

MAXSAT = 15

satLevel = 0
# MAXSAT set to arbitrary value right now. Change once all food items have assigned value.

# satlevel is a variable that changes as you consume food items. Will be compared to
# MAXSAT at game end.

def retry():
    print " "
    raw_input("You only know how to do the options presented to you. Try again." )
    # Trying to figure out how to just have an option to reenter a response without printing
    # the whole thing again.
    startbox()

def startbox():
    print " "
    print """
You slowly regain consciousness as you awaken, curled on a stone floor.
You stretch your little legs and begin shuffling around.
You're hungry, as always, and start to search for a snack.
It doesn't take long for you to realize you're at a dead end and the only 
thing you can do is go down the hallway in front of you.
    """

    # print the chunk of text below separately from the chunk of text above
    print "1. Go down hallway"
    print "2. Go back to sleep for a bit"
    print " "

    startboxChoice = raw_input("What do you do? ")

    if "1" in startboxChoice:
        #why doesn't the " " or " " in startboxChoice work correctly?
        choicePoint01()
    elif startboxChoice == "2":
        print " "
        print "You curl up and drift off to sleep..."
        sleep(1)
        startbox()
    else:
        print " "
        raw_input("You only know how to do the options presented to you. Try again." )
        # Trying to figure out how to just have an option to reenter a response without printing
        # the whole thing again.
        startbox()

def choicePoint01():
    print " "
    print """You quickly come to an intersection.
    In front of you, the hallway continues to stretch into the darkness. 
    You can faintly detect a cloying odor further down the hall. 
    The intersecting hallway branches off to your left and your right. 
    You do not smell anything in either direction."""

    print " "
    print "1. Keep going straight"
    print "2. Go down the hallway to your left"
    print "3. Go down the hallway to your right"
    print " "

    cp01Choice = raw_input("What do you do? ")

    if cp01Choice == "1":
        honeyRoomCP()
    elif cp01Choice == "2":
        swingRoomCP()
    elif cp01Choice == "3":
        rightHallCP()
    else:
        retry()

def swingRoomCP():
    print " "
    print """You quickly reach the entrance to a room.
    Inside you can hear the sound of occasional dripping into otherwise still water. 
    The doorway is open and you can scurry through. 
    Running parallel to the doorway is a sort of trellis. 
    You think you can climb it to reach the lintel over the doorway. 
    It's difficult to detect if there is anything useful on the lintel, but you are a strong climber, 
    especially where food is concerned."""

    print " "
    print "1. Go through the door"
    print "2. Climb up to the lintel"
    print "3. Turn around and go back"
    print " "

    swingRoomChoice = raw_input("What do you do? ")

    if swingRoomChoice == "1":
        swingRoomFloor()
    elif swingRoomChoice == "2":
        swingRaftersPort()
    elif swingRoomChoice == "3":
        choicePoint01()
    else:
        retry()

def honeyRoomCP():
    print " "
    print """You continue down the hallway for a long, long time. There are no doors or
    intersections or any other notable features as you scurry down the hall, but as you
    continue the sweet odor get stronger and stronger. You also hear a buzzing sound that
    gets louder as you continue down the hall. Eventually, you enter a room that is much too bright...
    so bright that you have difficulty seeing anything at all. The sweet smell is overpowering. 
    You follow it until you find structure dripping with a sticky, viscous liquid."""

    print " "
    print "1. Taste the liquid"
    print "2. Keep exploring"
    print "3. Go back to the intersection"
    print " "

    hrChoice = raw_input("What do you? ")

    if hrChoice == "1":
        honeyEat()
    elif hrChoice == "2":
        choicePoint02()
    elif hrChoice == "3":
        choicePoint01()
    else:
        retry()

def rightHallCP():
    print " "
    print """You scurry off to the right and begin to make your way down the hallway.
    Soon, your path forks to the left and to the right.
    Each path seems to spiral away from the other into the darkness below.
    At the base of the fork, you can smell cheese! Roquefort, to be exact.
    As you approach to take a nibble, you realize that the cheese is within a small cage, 
    preventing you from accessing it."""

    print " "
    print "1. Forget the cheese! Go down the leftward path."
    print "2. Forget the cheese! Go down the rightward path."
    print "3. Try gnawing on the bars of the cage to see if you can get to the cheese."
    print "4. Turn around and go back."
    print " "

    rightHallChoice = raw_input("What do you do? ")

    if rightHallChoice == "1":
        rhLeftPath()
    elif rightHallChoice == "2":
        rhRightPath()
    elif rightHallChoice == "3":
        rhGnaw()
    elif rightHallChoice == "4":
        choicePoint01()
    else:
        retry()

def swingRoomFloor():
    print """
    As you enter the room, you see that, rather than having a normal floor, there is a large pool 
    of stagnant water. You don't see any way of walking around it. There is a series of ropes hanging from 
    the rafters above, however. You reckon that with a running start you could probably grab one of the 
    ropes and try to scramble across.
    """

    print " "
    print "1. Run and jump"
    print "2. Turn around and go back"
    print " "

    srFloorChoice = raw_input("What do you do? ")

    if srFloorChoice == "1":
        swingRoomRopes()
    elif srFloorChoice == "2":
        swingRoomCP()
    else:
        retry()

def swingRaftersPort():
    print """
    When you reach the top of the lintel, you find a tiny portcullis in front of a tiny opening in the wall. 
    Just your size! Next to the portcullis you find a lever. There is also a depression in the wall that it looks 
    like you can poke your nose into. If there is any way of opening the gate, it is probably one of these.
    """

    print " "
    print "1. Nose-poke"
    print "2. Lever-press"
    print "3. Turn around and go back"
    print " "

    srRaftersChoice = raw_input("What do you do? ")

    if srRaftersChoice == "1":
        nosePoke()
    elif srRaftersChoice == "2":
        leverPress()
    elif srRaftersChoice == "3":
        swingRoomCP()
    else:
        retry()

def honeyEat():
    print """
    You approach the liquid gingerly and take a small taste. Honey! It tastes sweet and
    wonderful! As you greedily lap it up, the buzzing sound in the room intensifies and you begin
    to feel nervous. You feel something whoosh past your head and hear it humming angrily as you 
    freeze in your tracks. You feel sure that you need to make a quick getaway.
    """

    print " "
    print "1. Try to take a few more slurps of the delicious liquid before scurrying off."
    print "2. Cut your losses and run away now."
    print " "

    honeyChoice = raw_input("What do you do? ")

    if honeyChoice == "1":
        honeyStay()
    elif honeyChoice == "2":
        honeyGo()
    else:
        retry()

def choicePoint02():
    print "Choice point between stairs and warm, sleepy room goes here."

    cp02Choice = raw_input("What do you do? ")

    if cp02Choice == "1":
        warmSleepy()
    elif cp02Choice == "2":
        bottomStairs()
    else:
        retry()

def rhLeftPath():
    print "The dead end goes here. You go back."
    choicePoint02()
    #not sure I got this right...

def rhRightPath():
    print "Right path goes here."

def rhGnaw():
    print "Gnaw goes here."

def swingRoomRopes():
    print "Swing room ropes go here."

def nosePoke():
    print "Nose poke goes here."

def leverPress():
    print "Lever press goes here."

def honeyStay():
    print "Honey room stay goes here."

def honeyGo():
    print "Honey room go goes here."

def warmSleepy():
    print "Warm n' sleepy room goes here."

def bottomStairs():
    print "Bottom of stairs goes here."

def rhDeadEnd():
    print "Right hall dead end goes here."

def betterCheese():
    print "Better cheese room goes here."

def gnawCheese():
    print "Gnaw cheese goes here."


def functiongoeshere():
    print "At some point, real functions will go here."
    # Delete the above when all choice options have actually been written.


def satcompare():
    satRatio = satLevel / MAXSAT

    if satRatio >= 14:
        print "Some kind of final outcome will go here."
    elif satRatio >= 11:
        print "A different, and less desirable outcome will go here."
    elif satRatio >= 8:
        print "A different, and less desirable outcome will go here."
    elif satRatio >= 5:
        print "A different, and less desirable outcome will go here."
    else:
        print "A probably pretty bad outcome will go here."

startbox()
