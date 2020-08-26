# LAWBOT FUNCTIONS

# Import functions
from otherFuncs import removeSpace
import math

# List of all lawbot types
lawbotTypes = ["BOTTOMFEEDER", "BLOODSUCKER", "DOUBLETALKER", "AMBULANCECHASER", "BACKSTABBER", "SPINDOCTOR", "LEGALEAGLE", "BIGWIG"]

# Create constant dictionaries of jury notice amounts for each cog type
BOTTOMFEEDER = {"1":60, "2":80, "3":100, "4":120, "5":500}
BLOODSUCKER = {"2":100, "3":130, "4":160, "5":190, "6":800}
DOUBLETALKER = {"3":160, "4":210, "5":260, "6":310, "7":1300}
AMBULANCECHASER = {"4":260, "5":340, "6":420, "7":500, "8":2100}
BACKSTABBER = {"5":420, "6":550, "7":680, "8":810, "9":3400}
SPINDOCTOR = {"6":680, "7":890, "8":1100, "9":1310, "10":5500}
LEGALEAGLE = {"7":1100, "8":1440, "9":1780, "10":2120, "11":8900}
BIGWIG = {"8":1780, "9":2330, "10":2880, "11":3430, "12":14400, "13":1780,
"14":14400, "15":1780, "16":2330, "17":2880, "18":3430, "19":14400,
"20":1780, "21":2330, "22":2880, "23":3430, "24":3980, "25":4530,
"26":5080, "27":5630, "28":6180, "29":14400, "30":1780, "31":2330,
"32":2880, "33":3430, "34":3980, "35":4530, "36":5080, "37":5630,
"38":6180, "39":14400, "40":1780, "41":2330, "42":2880, "43":3430,
"44":3980, "45":4530, "46":5080, "47":5630, "48":6180, "49":14400, 
"50":0}

# Dict of dicts to access all cog dicts
lawbotDicts = {"BOTTOMFEEDER":BOTTOMFEEDER, "BLOODSUCKER":BLOODSUCKER, "DOUBLETALKER":DOUBLETALKER, "AMBULANCECHASER":AMBULANCECHASER, "BACKSTABBER":BACKSTABBER, "SPINDOCTOR":SPINDOCTOR, "LEGALEAGLE":LEGALEAGLE, "BIGWIG":BIGWIG}

# Dict of DA Office jury notices
DAnotices = {"A":564, "B":944, "C":1370, "D":1842}

# FUNCTION - Asks for the cog suit type and level, then stores them in variables
def askForCog():

    # Asks for cog type
    print("What cog are you on?")
    print("""(Enter one of the following: Bottom Feeder, Bloodsucker, Double Talker, Ambulance Chaser, Back Stabber, Spin Doctor, Legal Eagle, or Big Wig.)""")
    lawSuit = input().upper()
    lawSuit = removeSpace(lawSuit)

    # If not a type, ask again
    if lawSuit not in lawbotTypes:
        print("Oops ! That's not a Lawbot. Try typing a Lawbot.")
        lawSuit = input().upper()
        lawSuit = removeSpace(lawSuit)

    # Asks for cog level
    print("What level are you on?")
    lawLevel = input()

    # If not a number, ask again
    if lawLevel.isdigit() != True:
        print("Oops! Enter a number.")
        lawLevel = input()

    # If not in the specified Lawbot range (or negative), ask again
    if lawLevel not in lawbotDicts.get(lawSuit) or int(lawLevel) < 0:
        print("Oops! That's not a level for that cog. Try typing a correct level.")
        lawLevel = input()

    # Return a list containing the statistics of the suit desired
    return [lawSuit, lawLevel]

# FUNCTION - Prints the jury notices that you need for the specified cog promotion
def printNotices(lawStats):

    # First check if the level is 50 and terminate if so
    if lawStats[0] == "50":
        print("You don't need any more jury notices, silly! Congrats on max Lawbot!")
        return 0

    # Matches dictionary to cog type
    lawDict = lawbotDicts.get(lawStats[0])

    # Gets jury notices from corresponding dictionary
    noticesNeeded = lawDict.get(lawStats[1])

    # Prints jury notices
    print("For this cog promotion, you need " + str(noticesNeeded) + " jury notices.")

    # Asks if you already have some notices and prints how many you really need
    print("Do you already have some jury notices? (Enter quantity. Enter 0 if you have none.)")
    noticesAcquired = input()
    while True:
        if noticesAcquired.isdigit() != True:
            print("That's not a number! Try entering a number.")
            noticesAcquired = input()
            continue
        elif int(noticesAcquired) > noticesNeeded or int(noticesAcquired) < 0:
            print("That can't be right. Try entering a number that makes sense, please!")
            noticesAcquired = input()
            continue
        elif noticesAcquired != "0":
            noticesRemaining = noticesNeeded - int(noticesAcquired)
            print("So, you actually need " + str(noticesRemaining) + " jury notices.")
            break
        else:
            noticesRemaining = noticesNeeded
            break

    # Returns notices needed for further calculation
    return noticesRemaining

# FUNCTION - Calculates how many Office A (ONLY) are needed
def officeA(notices):

    numARaw = notices / DAnotices.get("A")
    numA = math.ceil(numARaw)
    if numA == 1:
        print("To do only Office As, you will need " + str(numA) + " OFFICE A to get all of your jury notices.")
    else:
        print("To do only Office As, you will need " + str(numA) + "OFFICE As to get all of your jury notices.")

# FUNCTION - Calculates how many Office B (ONLY) are needed
def officeB(notices):

    numBRaw = notices / DAnotices.get("B")
    numB = math.ceil(numBRaw)
    if numB == 1:
        print("To do only Office Bs, you will need " + str(numB) + " OFFICE B to get all of your jury notices.")
    else:
        print("To do only Office Bs, you will need " + str(numB) + " OFFICE Bs to get all of your jury notices.")

# FUNCTION - Calculates how many Office C (ONLY) are needed
def officeC(notices):

    numCRaw = notices / DAnotices.get("C")
    numC = math.ceil(numCRaw)
    if numC == 1:
        print("To do only Office Cs, you will need " + str(numC) + " OFFICE C to get all of your jury notices.")
    else:
        print("To do only Office Cs, you will need " + str(numC) + " OFFICE Cs to get all of your jury notices.")

# FUNCTION - Calculates how many Office D (ONLY) are needed
def officeD(notices):

    numDRaw = notices / DAnotices.get("D")
    numD = math.ceil(numDRaw)
    if numD == 1:
        print("To do only Office Ds, you will need " + str(numD) + " OFFICE D to get all of your jury notices.")
    else:
        print("To do only Office Ds, you will need " + str(numD) + " OFFICE Ds to get all of your jury notices.")

# FUNCTION - Calculates an ideal route for the least jury notice waste (Only A, B, and D because nobody uses C)
def idealOff(notices):

    # Calculates number of Ds first
    numDRaw = notices / DAnotices.get("D")
    numD = math.floor(numDRaw)

    # Gets remainder for Cs
    remainder = notices % DAnotices.get("D")
    ratio = remainder / DAnotices.get("D")
    if ratio > 0.7: # 70% is arbitrary; seems to be worth the extra time
        numD = numD + 1
        remainder = remainder - DAnotices.get("D")
        if remainder < 0:
            remainder = 0

    # Calculates number of Bs
    numBRaw = remainder / DAnotices.get("B")
    numB = math.floor(numBRaw)

    # Gets remainder again for As
    remainder2 = remainder % DAnotices.get("B")
    ratio2 = remainder2 / DAnotices.get("B")
    if ratio2 > 0.8: # 80% is also arbitrary; it is easier to do two quicker As than a B for a low amount
        numB = numB + 1
        remainder2 = remainder2 - DAnotices.get("B")
        if remainder2 < 0:
            remainder2 = 0

    # Calculates number of As to finish
    numARaw = remainder2 / DAnotices.get("A")
    numA = math.ceil(numARaw)

    # Prints ideal path
    print("Here is an ideal DA Office combo for you.")
    if numD == 1:
        DString = "OFFICE D"
    else:
        DString = "OFFICE Ds"

    if numB == 1:
        BString = "OFFICE B"
    else:
        BString = "OFFICE Bs"

    if numA == 1:
        AString = "OFFICE A"
    else:
        AString = "OFFICE As"

    print("To get all your jury notices, you will need " + str(numD) + " " + DString + ", " + str(numB) + " " + BString + ", and " + str(numA) + " " + AString + ".")

    # Calculates more to implement buildings if A may be too long
    remainderb = remainder2 % DAnotices.get("A")
    ratiob = remainderb / DAnotices.get("A")

    if ratiob < 0.2 and ratiob != 0: # 20% is arbitrary
        print("But because you only need " + str(math.ceil(remainderb)) + " more jury notices, it may be more efficient to \ncomplete a cog building or two instead of the last Office A! The choice is up to you.")