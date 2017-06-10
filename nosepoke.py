"""
This should give the user two choices, to poke their nose into an opening or to leave the room.
Each nose poke will increment a counter. When the counter reaches five, the user will be presented
with a reward option. They can choose to accept or reject. If they accept, it will increment their
satiation level by (some amount) and open an exit option that takes them forward while
simultaneously removing the previous exit option, which only allowed the to go backward.
"""

fakevariable = "This is a fake variable"

satLevel = 0
#take this out. it's just here to avoid error messages

frCount = 0

def postSchedRoom():
    print "This is just a placeholder to prevent error messages."

def swingRaftersPort():
    print "This is just a placeholder to prevent error messages."

def retry():
    print "This is just a placeholder to prevent error messages."

def nosePoke():
    
    print " "
    print
    """
The nose poke text goes here. You can choose 1 to nose-poke or 2 to turn around and go back.
    """
    print " "

    npChoice = raw_input("What do you do? ")

    if npChoice == "1":
        npProceed()
    elif npChoice == "2":
        swingRaftersPort()
    else:
        retry()


def npProceed():
    # trying to make a reusable bit of code for bumping up frCount and presenting a choice to
    # persist or not
    frCount += 1

    print " "
    print "Here you can choose to continue 1. nose-poking or 2. exit."
    print " "

    npPersist = raw_input("What do you do? ")

    if npPersist == "1":
        npProceed()
    elif npPersist == "2":
        swingRaftersPort()
    else:
        retry()


# not sure where in nesting to put the bit below yet.
# the code below should trigger if and only if the npChoice couonter reaches 5
if npChoice == 5:
    print 
    """
A food pellet pops out of an opening in the wall. As this happens, the door behind you shuts, but a new door
opens on the other side.
    """
    print " "
    print "1. Eat the pellet"
    print "2. Skip the pellet and go through the new door."
    print " "

    eatChoice = raw_input("What do you do? ")

    if eatChoice == "1":
        satLevel += 3
        #this increments a variable located in the main document

        print "Some copy about eating the pellet and a reference to how full you feel."
        print "Some copy about shuffling into the next room."

        postSchedRoom()
        #this will push them into the next room
        #the postSchedRoom function is in the main document and still needs to be written
    elif eatChoice == "2":

        print "Some copy about moving to the next room."

        postSchedRoom()

    else:
        retry()
