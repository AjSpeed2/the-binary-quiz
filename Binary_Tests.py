# Test for binary, hexadecimal, and 

from math import floor
import random


binaryNumber = ""
value = 0
hexaSymbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B" , "C", "D", "E", "F"] 

# The starting function that asks the user for the difficulty
def difficultyChoice():
    """Makes the user choose the max amount of bits they want their questions to contain"""
    howManyBits = input("How many bits would you like in the binary numbers? (Min of 4, max of 64, rounded to the next lowest multiple of 4)\n").lower().strip()
    if howManyBits.isnumeric() and int(howManyBits) in range(4, 65):
        return int(howManyBits)
    elif howManyBits.isnumeric():
        # If the value is numeric but doesnt pass the second condition
        print("Invalid range.")
        return 0
    else:
        # Type is probably a string
        print("Invalid input.")
        return 0
        

# Lets the user choose if the binary number can represent negative numbers
def integerChoice():
   """ Asks the user if they would like interger notation binary numbers to appear in their test. """
   choice = input("Would you like the binary numbers to have integer interpretation? (yes/no)\n").lower().strip()
   if choice == "yes":
       return True
   elif choice == "no":
       return False
   else:
       print("Invalid input.\n")
       return 2

def hexaChoice():
   """ Asks the user if they would like to include 16 bit and hexadecimal questions in their test. """
   choice = input("Would you like to include hexadecimal numbers in the test? (yes/no)\n").lower().strip()
   if choice == "yes":
       return True
   elif choice == "no":
       return False
   else:
       print("Invalid input.\n")
       return 2

# Generates the binary number
def generateBinaryNumber(isIntegerValue):
    """ Generates a binary number for the binary and integer questions """
    binaryNumber = ""
    counter = 0
    if isIntegerValue:
        binaryNumber += "1"
        counter += 1
    # Creates a random binary number depending on the difficulty
    while counter < maxBits:
        byte = str(random.randint(0, 1))
        binaryNumber += byte
        counter += 1
        
    # Calculates the value of the binary number
    value = 0
    choiceValue = random.randint(0, 2)
    

    if integerValues == False:
        for i in range(0, maxBits):
            value += int(binaryNumber[maxBits - 1 - i]) * (2 ** i)
    elif integerValues == True:
        if isIntegerValue == True and binaryNumber[0] == "1":
            for i in range(0, maxBits):
                value += int(binaryNumber[maxBits - 1 - i]) * (2 ** i)
            value = value - (2 ** len(binaryNumber))
        else:
            for i in range(0, maxBits):
                value += int(binaryNumber[maxBits - 1 - i]) * (2 ** i)
    # Adds a space in between the nibbles
    if len(binaryNumber) > 4:
        binaryNumber = ' '.join(binaryNumber[i:i+4] for i in range(0, len(binaryNumber), 4))
            
    numberAndValue = [binaryNumber, value, choiceValue]
    return numberAndValue

# Generates a binary question
def binaryQuestion():
    numberAndValue = generateBinaryNumber(False)
    binaryNumber = numberAndValue[0]
    value = numberAndValue[1]
    

    userGuess = int(input("What is the binary number " + str(binaryNumber) + " in decimal?\n"))
    if userGuess == value:
        print("Correct!\nNext one:")
        generateQuestion()
    else:
        print("Incorrect. Try again")
    
# Generates a hexidecimal question
def hexaQuestion():
    """Generates a hexadecimal question"""
    #Variable for the hexadecimal notation eg. A9B2#
    hexaNumber = ""
    # Variable for the total value in decimal
    decimalTotal = 0
    # Variable for the binary string
    binaryString = ""
    
    # Generates the hexadecimal number, the binary string of that number, and the decimal value of that number
    for i in range(4):
        value = random.randint(0, 15)
        hexaNumber += hexaSymbols[value]
        decimalTotal += value * (16 ** (3 - i))
        binaryString += str(bin(value)).removeprefix("0b").zfill(4)
        print
    
    # Generates the question from two different variations
    if random.random() == 0:
        # Asks the user to convert from hexidecimal to binary
        while True:
            binaryAnswer = input("What is "+ hexaNumber + "#" + " in binary?\n").replace(" ", "").strip()
            if binaryAnswer == binaryString:
                print("Correct!\n")
                break
            else:
                print("Incorrect, try again.\n")
            
        # Asks the user to convert from hexidecimal to decimal
        while True:
            decimalAnswer = int(input("What is the value of " + hexaNumber + "#" + " in decimal?\n"))
            if decimalAnswer == decimalTotal:
                print("Correct! Next one:\n")
                break
            else:
                print("Incorrect, try again.\n")
    else:
        # Asks the user to convert from binary to hexidecimal
        while True:
            if len(binaryString) > 4:
                binaryString = ' '.join(binaryString[i:i+4] for i in range(0, len(binaryString), 4))
            hexaAnswer = input("What is "+ binaryString + " in hexadecimal notation? (Use a # at the end)\n").strip()
            if hexaAnswer == hexaNumber + "#":
                print("Correct!\n")
                break
            else:
                print("Incorrect, try again.\n")
              
        # Asks the user to convert from hexidecimal to decimal
        while True:
            decimalAnswer = input("What is "+ hexaNumber + "#" + " in decimal?\n").strip()
            if decimalAnswer == decimalTotal:
                print("Correct! Next question:\n")
                break
            else:
                print("Incorrect, try again.\n")


    # Generates the next question
    generateQuestion()
    
# Generates an interger notation question
def integerQuestion():
    """Generates a integer question"""
    print("i")
    numberAndValue = generateBinaryNumber(True)
    binaryNumber = numberAndValue[0]
    value = numberAndValue[1]
    

    userGuess = int(input("What is the binary number " + str(binaryNumber) + " if it is an integer value?\n"))
    if userGuess == value:
        print("Correct!\nNext one:")
        generateQuestion()
    else:
        print("Incorrect. Try again")

# Chooses which question to ask randomly based on what the user selected
def generateQuestion():
    """Generates the quetion that will be used"""
    
    questionWeight = [2, 3, 4]
    
    if integerValues:
        questionWeight.insert(0,1)
        questionWeight.insert(0,0)
    if hexaValues:
       questionWeight.append(5)
       questionWeight.append(6)
    probability = random.randint(questionWeight[0], questionWeight[-1])
    if probability >= 2 and probability <=4:
        binaryQuestion()
    elif probability >= 5:
        hexaQuestion()
    else:
        integerQuestion()
        
        

#------------------------------------------------------------------------------------------

# Welcome user
print("Welcome to the binary numbers test! Created by Aiden Evans.\n")
# Begins the program by starting the function and returning a difficulty value
maxBits = difficultyChoice()
while maxBits == 0:
    maxBits = difficultyChoice()

# If the function returns 0, then restart the function
if maxBits % 4 != 0:
    maxBits = floor(maxBits / 4) * 4


# Asks the user if they would like to include questions with integer values
# These next two sequences return true or false values, so they return 2 if an invalid statement is input
integerValues = integerChoice()
while integerValues == 2:
    integerValues = integerChoice()
    
# Asks the user if they would like hexidecimal questions in their test
hexaValues = hexaChoice()
while hexaValues == 2:
    hexaValues = hexaChoice()


# Starts the program
generateQuestion()






