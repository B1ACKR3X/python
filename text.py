
# Imports any modules that I require for this to work.

import os
import time

# Variables python doesnt like meaning they need to be
# defined before assignment in a pass thru.

pt2 = False


# Sleeps for 1 second.

def time1():
    time.sleep(1)

# Sleeps for 2 seconds.

def time2():
    time.sleep(2)

# Clears the screen of trash.

def clear():
    for i in range(1,26):
        print ("\n")

# This function lets the user choose there name

def name(pt2):
    if pt2 == True:
        name = input("Before I begin with you, what is your name")
        clear(), protocol_D()
    else:
        name = input("Woah Woah Woah you have to walk before you can fly, whats your name")
        pt2()

# this is the 2nd part of the story before entering the building starting the main
# storyline this makes sure the user devol[es a basic back story and understand
# how the game works no matter what option the user picks this ensures
#cooperation resulting in lessuse of the restart function (clear) this could
# on some systems result in un used resorses and would then be vounerable to
# this code being used malicouly as a script kiddes lagger (your welcome github)

def pt2(name):
    pass

# this "protocol" shows the user how to begin/play the game


def protocol_D(name):
    pass



# The 1'st function requires for the game

'''
_________________________________________________________________
|                                                                 |
| ==================                                              |
| Side note to self:                                              |
| ==================                                              |
| --> Learn the pygame module                                     |
| --> learn basic math theorys required for 3d to start learning  |
|_________________________________________________________________|

 ________________________________________________________________________
{                                                                        }
{This function controls the first steps of the users journey introducing,}
{the user to the basic layer of the game (this could be expanded to be   }
{3d and/or longer)                                                       }
{________________________________________________________________________}

'''

def main():
    print("                ################################")
    print("                ######## Text Adventure! #######")
    print("                ################################")

    time2()
    
    '''
    the player is viewing the world from the dragons fly perspective
    this is important for stucturing the story as they have a shorter life span
    (this could be used depending on how long the story is) & (this can be used as
    a feature to limits players time spent on some of the parts of the story)
    '''

    print("Hello, sir/madam im sorry for the strange circumstances of,")
    print("this meeting but it is urgent.  The dragonfly protocol has been activated")
    
    q = int(input("-------------------\n1) What is the dragonfly protocol?\n2) Lets go!!"))

    if q == 1:
        name()
        pt2 = True
    elif 1 == 2:
        name()
    else:
        print("retry"), clear(), main()
    
    print("                               .-.")
    print("                              ()I()")
    print("                          ==.__:-:__.==")
    print("                         ==.__/~|~\__.==")
    print("                         ==._(  Y  )_.==")
    print("              .-'~~""~=--...,__\/|\/__,...--=~~~'-.")
    print("            (               ..=\=/=..               )")
    print("              `'-.        ,.-`;/=\ ;-.,_        .-'")
    print("                  `~-=-~` .-~` |=| `~-. `~-=-~`")
    print("                      .-~`    /|=|\    `~-.")
    print("                   .~`       / |=| \       `~")
    print("               .-~`        .'  |=|  `.        `~-.")
    print("              (`     _,.-=`    |=|    `=-.,_     `)")
    print("                `~~`           |=|           `~~`")
    print("                               |=|")
    print("                               |=|")
    print("                               |=|")
    print("                               \=/")
    print("                               /=\   ")
    print("                                ^")



    clear()
    
main()







##########################################################################3###########################
'''

For referance B1ACKR3X is my onine alias for git repos and forums



_____________________________________________________________________________________________________
|   _  \  \   \  /   /    |   _  \  /_ |     /   \     /      ||  |/  / |   _  \    |___ \  \  \ /  / 
|  |_)  |  \   \/   /     |  |_)  |  | |    /  ^  \   |  ,----'|  '  /  |  |_)  |     __) |  \  V  /  
|   _  <    \_    _/      |   _  <   | |   /  /_\  \  |  |     |    <   |      /     |__ <    >   <   
|  |_)  |     |  |        |  |_)  |  | |  /  _____  \ |  `----.|  .  \  |  |\  \----.___) |  /  .  \  
|______/      |__|        |______/   |_| /__/     \__\ \______||__|\__\ | _| `._____|____/  /__/ \__\
=====================================================================================================
'''
