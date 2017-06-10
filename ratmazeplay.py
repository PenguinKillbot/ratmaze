MAXSAT = 15

satLevel = 0
# MAXSAT set to arbitrary value right now. Change once all food items have assigned value.

# satlevel is a variable that changes as you consume food items. Will be compared to
# MAXSAT at game end.

def startbox():
    print """
    You slowly regain consciousness as you awaken, curled on a stone floor.
    You stretch your little legs and begin shuffling around.
    You're hungry, as always, and start to search for a snack.
    It doesn't take long for you to realize you're at a dead end and the only 
    thing you can do is go down the hallway in front of you.
    """

    print "1. Go down hallway"
    print "2. Go back to sleep for a bit"
    print " "

    startboxChoice = raw_input("What do you do? ")

    if "1" or "down hallway" in startboxChoice:
        choicePoint01()
    elif "2" or "sleep" in startboxChoice:
        startbox()
    else:
        print "You only know how to do the options presented to you. Try again."
        print " "
        print "What do you do? "



def choicePoint01():
    print "This is where choice point 1 goes."

startbox()



    def startboxChoiceFunc(startboxChoice):
        startboxChoice = raw_input("What do you do? ")

        if startboxChoice == "1" or "Go down hallway":
            choicePoint01()
        elif startboxChoice == "2" or "Go back to sleep for a bit":
            startbox()
        else:
            print "You only know how to do the options presented to you. Try again."
            print " "
            print "What do you do? "
    startboxChoiceFunc()