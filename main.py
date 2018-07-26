import os
from sortingTests import *

from colorama import init, Fore, Back, Style
init(convert=True)

# -------------------------------------------------------------------------
# Function: main()
# Description: Runs the main program
# -------------------------------------------------------------------------
def main():
    while True:
        printMenu()

        # get user input and test validity
        userInput = input("Please select an option: ")
        inputValid = testInput(userInput)
        print()

        # if the input is valid
        if inputValid:
            if userInput.lower() == "x":
                quit()
            elif userInput == "1":
                bubbleSortTest()
            elif userInput == "2":
                insertionSortTest()
            elif userInput == "3":
                selectionSortTest()
            elif userInput == "4":
                mergeSortTest()
            elif userInput == "5":
                quickSortTest()
            input("Press enter to continue...\n")
            os.system("cls") # will clear on Windows

        else:
            print("\nYou must make a valid selection")
            input("Press enter to continue...\n")
            os.system("cls") # will clear on Windows

# -------------------------------------------------------------------------
# Function: printMenu()
# Description: Prints the menu selection options for the user to view
# -------------------------------------------------------------------------
def printMenu():
        print("===================================================")
        print(Fore.YELLOW + "               TIMING TEST SELECTION               " + Style.RESET_ALL)
        print("===================================================")
        print("| 1 - Bubble Sort                                 |")
        print("| 2 - Insertion Sort                              |")
        print("| 3 - Selection Sort                              |")
        print("| 4 - Merge Sort                                  |")
        print("| 5 - Quick Sort                                  |")
        print("| X - eXit the program                            |")
        print("===================================================\n")

# -------------------------------------------------------------------------
# Function: testInput(userInput)
# Description: Ensures that user input is a valid selection via the menu.
#              Will return true if valid and false otherwise
# -------------------------------------------------------------------------
def testInput(userInput):
    validChars = "123456xX"
    
    if len(userInput) > 1 or len(userInput) == 0:
        return False
    else:
        if userInput in validChars:
            return True
        else:
            return False

main()
