# SELLBOT FUNCTIONS

# Import functions
from otherFuncs import removeSpace
import math

# List of all sellbot types
sellbotTypes = ["COLDCALLER", "TELEMARKETER", "NAMEDROPPER", "GLADHANDER", "MOVERANDSHAKER", "TWOFACE", "MINGLER", "MRHOLLYWOOD"]

# Create constant dictionaries of merit amounts for each cog type
# (Manually inputted from known source)
COLDCALLER = {"1":20, "2":30, "3":40, "4":50, "5":200}
TELEMARKETER = {"2":40, "3":50, "4":60, "5":70, "6":300}
NAMEDROPPER = {"3":60, "4":80, "5":100, "6":120, "7":300}
GLADHANDER = {"4":100, "5":130, "6":160, "7":190, "8":800}
MOVERANDSHAKER ={"5":160, "6":210, "7":260, "8":310, "9":1300}
TWOFACE = {"6":260, "7":340, "8":420, "9":500, "10":2100}
MINGLER = {"7":420, "8":550, "9":680, "10":810, "11":3400}
MRHOLLYWOOD = {"8":680, "9":890, "10":1100, "11":1310, "12":5500, "13":680, 
"14":5500, "15":680, "16":890, "17":1100, "18":1310, "19":5500, "20":680,
"21":890, "22":1100, "23":1310, "24":1520, "25":1730, "26":1940, "27":2150,
"28":2360, "29":5500, "30":680, "31":890, "32":1100, "33":1310, "34":1520, 
"35":1730, "36":1940, "37":2150, "38":2360, "39":5500, "40":680, "41":890, 
"42":1100, "43":1310, "44":1520, "45":1730, "46":1940, "47":2150, "48":2360, 
"49":5500, "50":0}

# Dict of dicts to access all cog dicts
sellbotDicts = {"COLDCALLER":COLDCALLER, "TELEMARKETER":TELEMARKETER, "NAMEDROPPER":NAMEDROPPER, "GLADHANDER":GLADHANDER, "MOVERANDSHAKER":MOVERANDSHAKER, "TWOFACE":TWOFACE, "MINGLER":MINGLER, "MRHOLLYWOOD":MRHOLLYWOOD}

# Dictionary of factory merits
factoryMerits = {"short":480, "long":776, "side":584}

# FUNCTION - Asks for the cog suit type and level, then stores them in variables
def askForCog():

    # Asks for cog type
    print("What cog are you on?")
    print("""(Enter one of the following: Cold Caller, Telemarketer, Name Dropper, Glad Hander, Mover and Shaker, Two Face, Mingler, or Mr Hollywood.)""")
    sellSuit = input().upper()
    sellSuit = removeSpace(sellSuit)

    # If not a type, ask again
    if sellSuit not in sellbotTypes:
        print("Oops! That's not a Sellbot. Try typing a Sellbot.")
        sellSuit = input().upper()
        sellSuit = removeSpace(sellSuit)

    # Asks for cog level
    print("What level are you on?")
    sellLevel = input()

    # If not a number, ask again
    if sellLevel.isdigit() != True:
        print("Oops! Enter a number.")
        sellLevel = input()

    # If not in the specified Sellbot range (or negative), ask again
    if sellLevel not in sellbotDicts.get(sellSuit) or int(sellLevel) < 0:
        print("Oops! That's not a level for that cog. Try typing a correct level.")
        sellLevel = input()

    # Return a list containing the statistics of the suit desired
    return [sellSuit, sellLevel]

# FUNCTION - Prints the merits that you need for the specified cog promotion
def printMerits(sellStats):

    # First check if the level is 50 and terminate if so
    if sellStats[1] == "50":
        print("You don't need anymore merits, silly! Congrats on max Sellbot!")
        return 0

    # Matches dictionary to cog type
    sellDict = sellbotDicts.get(sellStats[0])

    # Gets merits from corresponding dictionary
    meritsNeeded = sellDict.get(sellStats[1])

    # Prints merits
    print("For this cog promotion, you need " + str(meritsNeeded) + " merits.")

    # Asks if you already have some merits and prints how many you really need
    print("Do you already have some merits? (Enter quantity. Enter 0 if you have none.)")
    meritsAcquired = input()
    while True:
        if meritsAcquired.isdigit() != True:
            print("That's not a number! Try entering a number.")
            meritsAcquired = input()
            continue
        elif int(meritsAcquired) > meritsNeeded or int(meritsAcquired) < 0:
            print("That can't be right. Try entering a number that makes sense, please!")
            meritsAcquired = input()
            continue
        elif meritsAcquired != "0":
            meritsRemaining = meritsNeeded - int(meritsAcquired)
            print("So, you actually need " + str(meritsRemaining) + " merits.")
            break
        else:
            meritsRemaining = meritsNeeded
            break

    # Returns merits needed for further calculation
    return meritsRemaining

# FUNCTION - Calculates how many short factories (ONLY) are needed
def shortFact(merits):

    numShortsRaw = merits / factoryMerits.get("short")
    numShorts = math.ceil(numShortsRaw)
    if numShorts == 1:
        print("To do only short factories, you will need " + str(numShorts)  + " SHORT FACTORY to get all of your merits.")
    else:
        print("To do only short factories, you will need " + str(numShorts)  + " SHORT FACTORIES to get all of your merits.")

# FUNCTION - Calculates how many long factories (ONLY) are needed
def longFact(merits):

    numLongsRaw = merits / factoryMerits.get("long")
    numLongs = math.ceil(numLongsRaw)
    if numLongs == 1:
        print("To do only long factories, you will need " + str(numLongs) + " LONG FACTORY to get all of your merits.")
    else:
        print("To do only long factories, you will need " + str(numLongs) + " LONG FACTORIES to get all of your merits.")

# FUNCTION - Calculates how many side factories (ONLY) are needed
def sideFact(merits):

    numSidesRaw = merits / factoryMerits.get("side")
    numSides = math.ceil(numSidesRaw)
    if numSides == 1:
        print("To do only side factories, you will need " + str(numSides) + " SIDE FACTORY to get all of your merits.")
    else:
        print("To do only side factories, you will need " + str(numSides) + " SIDE FACTORIES to get all of your merits.")

# FUNCTION - Calculates an ideal route for the least merit waste
def idealFact(merits):

    # Calculates number of longs first
    numLongsRaw = merits / factoryMerits.get("long")
    numLongs = math.floor(numLongsRaw)

    # Gets remainder for shorts
    remainder = merits % factoryMerits.get("long")
    ratio = remainder / factoryMerits.get("long")
    if ratio > 0.6: # 60% is arbitrary; seems to be worth the extra effort
        numLongs = numLongs + 1
        remainder = remainder - factoryMerits.get("long")
        if remainder < 0:
            remainder = 0

    # Calculates number of shorts to finish
    numShortsRaw = remainder / factoryMerits.get("short")
    numShorts = math.ceil(numShortsRaw)

    # Prints ideal path
    print("Here is an ideal factory path for you (made of longs and shorts, because who actually uses sides).")
    if numLongs == 1:
        longString = "LONG FACTORY"
    else:
        longString = "LONG FACTORIES"

    if numShorts == 1:
        shortString = "SHORT FACTORY"
    else:
        shortString = "SHORT FACTORIES"
        
    print("To get all your merits, you will need " + str(numLongs) + " " +  longString + " and " + str(numShorts) + " " + shortString + ".")

    # Calculates more to implement buildings if short may be too long
    remainder2 = remainder % factoryMerits.get("short")
    ratio2 = remainder2 / factoryMerits.get("short")

    if ratio2 < 0.4 and ratio2 != 0: # 40% is arbitrary, seems to be excessive in some cases
        print("But because you only need " + str(remainder2) + " more merits, it may be more efficient to \ncomplete a cog building or two instead of one short factory! The choice is up to you.")
        