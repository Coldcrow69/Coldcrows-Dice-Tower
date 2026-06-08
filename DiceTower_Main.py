# Metadata
__app_name__ = "Coldcrow's Dice Tower"
__version__ = "1.2"
__author__ = "Coldcrow"

# import modules
import re
import sys
import time
import random
import msvcrt
import subprocess

# Matches a roll request like "1d20+4", "2d6-1", or "1d100". Whitespace and
# case are normalized away before matching, so " 1 D 20 + 4 " is valid.
ROLL_PATTERN = re.compile(r"^(\d+)d(\d+)([+-]\d+)?$")


def parseRollRequest(rollRequest):
    """Parse a roll string into (quantity, size, modifier).

    Returns (0, 0, 0) for any input that is not a well-formed roll request.
    """
    match = ROLL_PATTERN.match(rollRequest.replace(" ", "").lower())
    if not match:
        return (0, 0, 0)
    quantity, size, modifier = match.groups()
    return (int(quantity), int(size), int(modifier) if modifier else 0)


def diceTower(diceQuantity, diceSize, diceModifier=0):
    """Roll diceQuantity dice of diceSize sides. Returns ([rolls], modified sum)."""
    if diceQuantity <= 0 or diceSize <= 0:
        return ([], diceModifier)
    rolls = [random.randint(1, diceSize) for _ in range(diceQuantity)]
    return (rolls, sum(rolls) + diceModifier)


def clear_screen():
    """Clear the console (Windows). Replaces the deprecated os.system('cls')."""
    subprocess.run(["cmd", "/c", "cls"], check=False)


def header(title, subtitle):
    """Clear the screen and print a standard boxed header."""
    clear_screen()
    print("==================================")
    print("       | {} |".format(title))
    print("      | {} |".format(subtitle))
    print("==================================\n")


def pause(warning="Roll data will be lost."):
    """Wait for a keypress, warning the user that on-screen results will clear."""
    print("Press any key to continue... WARNING: {}".format(warning))
    msvcrt.getch()


def standardRoller():
    """Prompt for free-form roll requests (e.g. "1d20+4") and roll them."""
    while True:
        header("STANDARD ROLLER", " ROLL YOUR DICE ")
        print("Ex. 1D20+4 OR q to quit.\n")
        rollRequest = input("Your Roll: ")
        if rollRequest.lower() == "q":
            return

        print("\nRolling {}...\n".format(rollRequest))
        quantity, size, modifier = parseRollRequest(rollRequest)
        rolls, total = diceTower(quantity, size, modifier)
        print("Your dice rolls were... {}\n".format(rolls))
        print("Your total modified roll is... {}\n".format(total))
        pause()


def moonSugar():
    """Roll the Moon Sugar premade effect and print its modifier tables."""
    print("\nRolling 1d100 (advantage) for dankness...\n")
    dankRoll, _ = diceTower(2, 100)
    dankness = sorted(dankRoll)[1]

    statMod = 0
    if dankness == 1:
        hpMod = -5
    elif dankness <= 25:
        hpMod = diceTower(1, 4)[1]
    elif dankness <= 50:
        hpMod = diceTower(1, 6)[1]
    elif dankness <= 75:
        hpMod = diceTower(1, 8)[1]
        statMod = diceTower(2, 4)[1]
    elif dankness <= 99:
        hpMod = diceTower(1, 10)[1]
        statMod = diceTower(2, 4)[1]
    else:
        hpMod = diceTower(1, 20)[1]
        statMod = diceTower(2, 4)[1]

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
    pause("Results will be cleared.")


def premadeRoller():
    """Menu of hardcoded premade rolls."""
    while True:
        header("PREMADE ROLLER", "MAKE A SELECTION")
        print("1...    Moon Sugar\n")
        print("2...    Quit to Menu\n")
        print("==================================\n")
        selection = input("Enter your selection: ")
        if selection == "1":
            moonSugar()
        elif selection == "2":
            return
        else:
            print("\nINVALID SELECTION")
            time.sleep(2)


def menu():
    """Main menu. Loops until the user chooses to exit."""
    while True:
        clear_screen()
        print(r"""
           
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
        selection = input("Enter your selection: ")
        if selection == "1":
            standardRoller()
        elif selection == "2":
            premadeRoller()
        elif selection == "3":
            sys.exit()
        else:
            print("\nINVALID SELECTION")
            time.sleep(2)


# start the program
if __name__ == "__main__":
    menu()
