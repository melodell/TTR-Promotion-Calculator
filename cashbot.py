# CASHBOT FUNCTIONS

# Import functions
from otherFuncs import removeSpace
import math

# List of all cashbot types
cashbotTypes = ["SHORTCHANGE", "PENNYPINCHER", "TIGHTWAD", "BEANCOUNTER", "NUMBERCRUNCHER", "MONEYBAGS", "LOANSHARK", "ROBBERBARON"]

# Create constant dictionaries of cogbuck amounts for each cog type
# (Manually inputted from source)
SHORTCHANGE = {"1":40, "2":50, "3":60, "4":70, "5":300}
PENNYPINCHER = {"2":60, "3":80, "4":100, "5":120, "6":500}
TIGHTWAD = {"3":100, "4":130, "5":160, "6":190, "7":800}
BEANCOUNTER = {"4":160, "5":210, "6":260, "7":310, "8":1300}
NUMBERCRUNCHER = {"5":260, "6":340, "7":420, "8":500, "9":2100}
MONEYBAGS = {"6":420, "7":550, "8":680, "9":810, "10":3400}
LOANSHARK = {"7":680, "8":890, "9":1100, "10":1310, "11":5500}
ROBBERBARON = {"8":1100, "9":1440, "10":1780, "11":2120, "12":8900, "13":1100, 
"14":8900, "15":1100, "16":1440, "17":1780, "18":2120, "19":8900, "20":1100, 
"21":1440, "22":1780, "23":2120, "24":2460, "25":2800, "26":3140, "27":3480,
"28":3820, "29":8900, "30":1100, "31":1440, "32":1780, "33":2120, "34":2460,
"35":2800, "36":3140, "37":3480, "38":3820, "39":8900, "40":1100, "41":1440, 
"42":1780, "43":2120, "44":2460, "45":2800, "46":3140, "47":3480, "48":3820,
"49":8900, "50":0}

# Dict of dicts to access all cog dicts
cashbotDicts = {"SHORTCHANGE":SHORTCHANGE, "PENNYPINCHER":PENNYPINCHER, "TIGHTWAD":TIGHTWAD, "BEANCOUNTER":BEANCOUNTER, "NUMBERCRUNCHER":NUMBERCRUNCHER, "MONEYBAGS":MONEYBAGS, "LOANSHARK":LOANSHARK, "ROBBERBARON":ROBBERBARON}

# Dictionaries of mint cogbucks (one for minimum, one for maximum)
minMintCogbucks = {"coin":356, "dollar":679, "bullion":1202}
maxMintCogbucks = {"coin":544, "dollar":1004, "bullion":1496}

# FUNCTION - Asks for the cog suit type and level, then stores them in variables
def askForCog():
    
    # Asks for cog type
    print("What cog are you on?")
    print("""(Enter one of the following: Short Change, Penny Pincher, Tightwad, Bean Counter, Number Cruncher, Money Bags, Loan Shark, or Robber Baron.""")
    cashSuit = input().upper()
    cashSuit = removeSpace(cashSuit)

    # If not a type, ask again
    if cashSuit not in cashbotTypes:
        print("Oops! That's not a Cashbot. Try typing a Cashbot.")
        cashSuit = input().upper()
        cashSuit = removeSpace(cashSuit)

    # Asks for cog level
    print("What level are you on?")
    cashLevel = input()

    # If not a number, ask again
    if cashLevel.isdigit() != True:
        print("Oops! Enter a number.")
        cashLevel = input()

    # If not in the specified Cashbot range (or negative), ask again
    if cashLevel not in cashbotDicts.get(cashSuit) or int(cashLevel) < 0:
        print("Oops! That's not a level for that cog. Try typing a correct level.")
        cashLevel = input()

    # Return a list containing the statistics of the suit desired
    return [cashSuit, cashLevel]

# FUNCTION - Prints the cogbucks that you need for the specified cog promotion
def printCogbucks(cashStats):

    # First check if the level is 50 and terminate if so
    if cashStats[1] == "50":
        print("You don't need anymore cogbucks, silly! Congrats on max Cashbot!")
        return 0

    # Matches dictionary to cog type
    cashDict = cashbotDicts.get(cashStats[0])

    # Gets cogbucks from corresponding dictionary
    cogbucksNeeded = cashDict.get(cashStats[1])

    # Prints cogbucks
    print("For this cog promotion, you need " + str(cogbucksNeeded) + " cogbucks.")

    # Asks if you already have some cogbucks and prints how many you really need
    print("Do you already have some cogbucks? (Enter quantity. Enter 0 if you have none.)")
    cogbucksAcquired = input()
    while True:
        if cogbucksAcquired.isdigit() != True:
            print("That's not a number! Try entering a number.")
            cogbucksAcquired = input()
            continue
        elif int(cogbucksAcquired) > cogbucksNeeded or int(cogbucksAcquired) < 0:
            print("That can't be right. Try entering a number that makes sense, please!")
            cogbucksAcquired = input()
            continue
        elif cogbucksAcquired != "0":
            cogbucksRemaining = cogbucksNeeded - int(cogbucksAcquired)
            print("So, you actually need " + str(cogbucksRemaining) + " cogbucks.")
            break
        else:
            cogbucksRemaining = cogbucksNeeded
            break

    # Returns cogbucks needed for further calculation
    return cogbucksRemaining

# FUNCTION - Calculates how many coin mints (ONLY) are needed
def coinMint(bucks):

    numCoinsMinRaw = bucks / minMintCogbucks.get("coin")
    numCoinsMin = math.ceil(numCoinsMinRaw)

    numCoinsMaxRaw = bucks / maxMintCogbucks.get("coin")
    numCoinsMax = math.ceil(numCoinsMaxRaw)

    if numCoinsMin == 1:
        print("To do only coin mints, you will need " + str(numCoinsMin) + " COIN MINT to get all of your cogbucks.")
    
    elif numCoinsMax == 1:
        print("To do only coin mints, you will need at least " + str(numCoinsMax) + " COIN MINT to get all of your cogbucks.")
        print("HOWEVER, you may need up to " + str(numCoinsMin) + " COIN MINTS to get them all if you do not get the maximum output.")

    else:
        print("To do only coin mints, you will need at least " + str(numCoinsMax) + " COIN MINTS to get all of your cogbucks.")
        print("HOWEVER, you may need up to " + str(numCoinsMin) + " COIN MINTS to get them all if you do not get the maximum output.")

# FUNCTION - Calculates how many dollar mints (ONLY) are needed
def dollarMint(bucks):

    numDollMinRaw = bucks / minMintCogbucks.get("dollar")
    numDollMin = math.ceil(numDollMinRaw)

    numDollMaxRaw = bucks / maxMintCogbucks.get("dollar")
    numDollMax = math.ceil(numDollMaxRaw)

    if numDollMin == 1:
        print("To do only dollar mints, you will need " + str(numDollMin) + " DOLLAR MINT to get all of your cogbucks.")
    
    elif numDollMax == 1:
        print("To do only dollar mints, you will need at least " + str(numDollMax) + " DOLLAR MINT to get all of your cogbucks.")
        print("HOWEVER, you may need up to " + str(numDollMin) + " DOLLAR MINTS to get them all if you do not get the maximum output.")

    else:
        print("To do only dollar mints, you will need at least " + str(numDollMax) + " DOLLAR MINTS to get all of your cogbucks.")
        print("HOWEVER, you may need up to " + str(numDollMin) + " DOLLAR MINTS to get them all if you do not get the maximum output.")

# FUNCTION - Calculates how many bullion mints (ONLY) are needed
def bullionMint(bucks):

    numBullMinRaw = bucks / minMintCogbucks.get("bullion")
    numBullMin = math.ceil(numBullMinRaw)

    numBullMaxRaw = bucks / maxMintCogbucks.get("bullion")
    numBullMax = math.ceil(numBullMaxRaw)

    if numBullMin == 1:
        print("To do only bullion mints, you will need " + str(numBullMin) + " BULLION MINT to get all of your cogbucks.")
    
    elif numBullMax == 1:
        print("To do only bullion mints, you will need at least " + str(numBullMax) + " BULLION MINT to get all of your cogbucks.")
        print("HOWEVER, you may need up to " + str(numBullMin) + " BULLION MINTS to get them all if you do not get the maximum output.")

    else:
        print("To do only bullion mints, you will need at least " + str(numBullMax) + " BULLION MINTS to get all of your cogbucks.")
        print("HOWEVER, you may need up to " + str(numBullMin) + " BULLION MINTS to get them all if you do not get the maximum output.")

# FUNCTION - Calculates an ideal route for the least cogbuck waste (no risks, so only min numbers)
def idealMint(bucks):

    # Calculates number of bullions first
    numBullRaw = bucks / minMintCogbucks.get("bullion")
    numBull = math.floor(numBullRaw)

    # Gets remainder for dollars
    remainder = bucks % minMintCogbucks.get("bullion")
    ratio = remainder / minMintCogbucks.get("bullion")
    if ratio > 0.8: # 80% is arbitrary; seems to be worth the big-time effort that comes with a bullion mint
        numBull = numBull + 1
        remainder = remainder - minMintCogbucks.get("bullion")
        if remainder < 0:
            remainder = 0

    # Calculates number of dollars
    numDollRaw = remainder / minMintCogbucks.get("dollar")
    numDoll = math.floor(numDollRaw)

    # Gets remainder again for coins
    remainder2 = remainder % minMintCogbucks.get("dollar")
    ratio2 = remainder2 / minMintCogbucks.get("dollar")
    if ratio2 > 0.6: # 60% is also arbitrary
        numDoll = numDoll + 1
        remainder2 = remainder2 - minMintCogbucks.get("dollar")
        if remainder2 < 0:
            remainder2 = 0

    # Calculates number of coins to finish
    numCoinsRaw = remainder2 / minMintCogbucks.get("coin")
    numCoins = math.ceil(numCoinsRaw)

    # Prints ideal path
    print("Here is an ideal mint path for you.")
    if numBull == 1:
        bullString = "BULLION MINT"
    else:
        bullString = "BULLION MINTS"

    if numDoll == 1:
        dollString = "DOLLAR MINT"
    else:
        dollString = "DOLLAR MINTS"

    if numCoins == 1:
        coinString = "COIN MINT"
    else:
        coinString = "COIN MINTS"    

    print("To get all your cogbucks, you will need *AT MOST* " + str(numBull) + " " + bullString + ", " + str(numDoll) + " " + dollString + ", and " + str(numCoins) + " " + coinString + " to be safe.")

    # Calculates more to implement buildings if coin may be too long
    remainderb = remainder2 % minMintCogbucks.get("coin")
    ratiob = remainderb / minMintCogbucks.get("coin")

    if ratiob < 0.3 and ratiob != 0: # 30% is arbitrary, seems to be excessive in some cases
        print("But because you only need " + str(math.ceil(remainderb)) + " more cogbucks, it may be more efficient to \ncomplete a cog building or two instead of one coin mint! The choice is up to you.")