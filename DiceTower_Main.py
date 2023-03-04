#Metadata
__name__ = "Coldcrow's Dice Tower"
__version__ = "1.0"
__author__ = "Coldcrow"

#import modules
import os
import time
import random
import msvcrt
import sys

#define parseRollRequest. Takes custom user input string, removes whitespace, converts to lower, and outputs 3 integers for number of dice to roll, size of dice, and math modifier.
def parseRollRequest(rollRequest):
    diceQuantity = 0
    diceSize = 0
    diceModifier = 0
    try:
        rollRequest = rollRequest.replace(" ", "").lower()
        diceQuantity = int(rollRequest[0:rollRequest.find('d')])
        if '+' in rollRequest:
            diceSize = int(rollRequest[rollRequest.find('d') + 1:rollRequest.find('+')])
            diceModifier = int(rollRequest[rollRequest.find('+') + 1:len(rollRequest) + 1])
        elif '-' in rollRequest:
            diceSize = int(rollRequest[rollRequest.find('d') + 1:rollRequest.find('-')])
            diceModifier = int(rollRequest[rollRequest.find('-') + 1:len(rollRequest) + 1]) * -1
        else:
            diceSize = int(rollRequest[rollRequest.find('d') + 1:len(rollRequest) + 1])
        return(diceQuantity,diceSize,diceModifier)
    except:
        return(0,0,0)

#define diceTower. Takes 3 integer inputs for dice quantity, dice size, and math modifier, rolls the specified number of dice using randint(), and produces a sum total including the math modifier. Returns a tuple in the form of ([list of rolls], sum total)
def diceTower(diceQuantity,diceSize,diceModifier):
    myRolls = []
    myRollsSum = 0
    while diceQuantity > 0:
        myRolls.append(random.randint(1,diceSize))
        diceQuantity -= 1
    myRollsSum = sum(myRolls) + diceModifier
    return(myRolls,myRollsSum)

#define standardRoller. Produces a menu where a user can enter a string such as "1d4+20" which will be passed to the parseRollRequest function to be scrubbed before the parsed version is passed to diceTower to be rolled. Prints the result of the dice rolls and the sum total.
def standardRoller():
    rollRequest = ""
    myResult = []
    os.system("cls")
    print("==================================")
    print("       | STANDARD ROLLER |")
    print("       | ROLL YOUR DICE  |")
    print("==================================\n")
    print("Ex. 1D20+4 OR q to quit.\n")
    rollRequest = input("Your Roll: ")
    if rollRequest.lower() == 'q':
        menu()
    else:
        print("")
        print("Rolling {}...\n".format(rollRequest))
        rollRequest = parseRollRequest(rollRequest)
        myResult = diceTower(rollRequest[0],rollRequest[1],rollRequest[2])
        print("Your dice rolls were... {}\n".format(myResult[0]))
        print("Your total modified roll is... {}\n".format(myResult[1]))
        print("Press any key to continue... WARNING: Roll data will be lost.")
        msvcrt.getch()
        standardRoller()

#define premadeRoller. Holds hardcoded premades which pass rolls to diceTower and print the necessary output information. At a later date this function should be split into a premadeRollerMenu, and a separate function for each premade roll.
def premadeRoller():
    menuSelection = ""
    dankRoll = []
    dankness = 0
    statMod = 0
    hpMod = 0
    os.system("cls")
    print("==================================")
    print("       | PREMADE ROLLER |")
    print("      | MAKE A SELECTION |")
    print("==================================\n")
    print("1...    Moon Sugar\n")
    print("2...    Quit to Menu\n")
    print("==================================\n")
    try:
        menuSelection = int(input("Enter your selection: "))
        if menuSelection == 1:
            print("")
            print("Rolling 1d100 (advantage) for dankness...\n")
            dankRoll = diceTower(2,100,0)
            dankness = sorted(dankRoll[0])[1]
            if dankness == 1:
                hpMod = -5
            elif dankness in range(2,26,1):
                hpMod = diceTower(1,4,0)[1]
            elif dankness in range(26,51,1):
                hpMod = diceTower(1,6,0)[1]
            elif dankness in range(51,76,1):
                hpMod = diceTower(1,8,0)[1]
                statMod = diceTower(2,4,0)[1]
            elif dankness in range(76,100,1):
                hpMod = diceTower(1,10,0)[1]
                statMod = diceTower(2,4,0)[1]
            else:
                hpMod = diceTower(1,20,0)[1]
                statMod = diceTower(2,4,0)[1]
            print("You rolled {} for dankness.\n".format(dankness))
            print("A list of effects is found below. These effects last 1 hour.\n")
            print("==================================\n")
            print("GLOBAL MODIFIERS:")
            print("- All reactions are performed at disadvantage w/ normalized DC 12.")
            print("- Disadvantage on initiative.")
            print("- Disadvantage on DEX checks.")
            print("- Disadvantage on WIS checks.")
            print("- Disadvantage on INT checks.\n")
            print("==================================\n")
            print("STAT MODIFIERS:")
            print("- Subtract {} among your WIS and/or INT.".format(statMod))
            print("- Add {} among your DEX, STR, and/or CHA.\n".format(statMod))
            print("==================================\n")
            print("HP MODIFIERS:")
            print("- Add {} to your HP MAX and CURRENT HP.\n".format(hpMod))
            print("==================================\n")
            print("Press any key to continue... WARNING: Results will be cleared.")
            msvcrt.getch()
            premadeRoller()
        elif menuSelection == 2:
            menu()
        else:
            raise ValueError
    except ValueError:
        print("\nINVALID SELECTION")
        time.sleep(2)
        premadeRoller()
    rollRequest = input("Your Roll: ")
    if rollRequest.lower() == 'q':
        menu()
    else:
        print("")
        print("Rolling {}...\n".format(rollRequest))
        rollRequest = parseRollRequest(rollRequest)
        myResult = diceTower(rollRequest[0],rollRequest[1],rollRequest[2])
        print("Your dice rolls were... {}\n".format(myResult[0]))
        print("Your total modified roll is... {}\n".format(myResult[1]))
        print("Press any key to continue... WARNING: Roll data will be lost.")
        msvcrt.getch()
        standardRoller()

#define menu. This acts as the main menu using a basic ASCII art GUI, accepting user input to choose a function of the program.
def menu():
    menuSelection = ""
    os.system("cls")
    print("""
   ____           _       _                                    _       
  / ___|   ___   | |   __| |   ___   _ __    ___   __      __ ( )  ___ 
 | |      / _ \  | |  / _` |  / __| | '__|  / _ \  \ \ /\ / / |/  / __|
 | |___  | (_) | | | | (_| | | (__  | |    | (_) |  \ V  V /      \__ |
  \____|  \___/  |_|  \__,_|  \___| |_|     \___/    \_/\_/       |___/
  ____    _                     _____                                  
 |  _ \  (_)   ___    ___      |_   _|   ___   __      __   ___   _ __ 
 | | | | | |  / __|  / _ \       | |    / _ \  \ \ /\ / /  / _ \ | '__|
 | |_| | | | | (__  |  __/       | |   | (_) |  \ V  V /  |  __/ | |   
 |____/  |_|  \___|  \___|       |_|    \___/    \_/\_/    \___| |_|                                                                        

    """)
    print("==================================")
    print("""          | MAIN MENU |
      | MAKE A SELECTION |""")
    print("==================================\n")
    print("1...    Standard Roller\n")
    print("2...    Premade Roller\n")
    print("3...    Exit Program\n")
    print("==================================\n")
    try:
        menuSelection = int(input("Enter your selection: "))
        if menuSelection == 1:
            standardRoller()
        elif menuSelection == 2:
            premadeRoller()
        elif menuSelection == 3:
            sys.exit()
        else:
            raise ValueError
    except ValueError:
        print("\nINVALID SELECTION")
        time.sleep(2)
        menu()

#start the program
menu()