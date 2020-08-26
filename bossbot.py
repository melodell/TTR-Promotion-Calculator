# BOSSBOT FUNCTIONS

# Import functions
from otherFuncs import removeSpace
import math

# List of all Bossbot types
bossbotTypes = ["FLUNKY", "PENCILPUSHER", "YESMAN", "MICROMANAGER", "DOWNSIZER", "HEADHUNTER", "CORPORATERAIDER", "BIGCHEESE"]

# Create constant dictionaries of stock option amounts for each cog types
FLUNKY = {"1":100, "2":130, "3":160, "4":190, "5":800}
PENCILPUSHER = {"2":160, "3":210, "4":260, "5":310, "6":1300}
YESMAN = {"3":260, "4":340, "5":420, "6":500, "7":2100}
MICROMANAGER = {"4":420, "5":550, "6":680, "7":810, "8":3400}
DOWNSIZER = {"5":680, "6":890, "7":1100, "8":1310, "9":5500}
HEADHUNTER = {"6":1100, "7":1440, "8":1780, "9":2120, "10":8900}
CORPORATERAIDER = {"7":1780, "8":2330, "9":2880, "10":3430, "11":14400}
BIGCHEESE = {"8":2880, "9":3770, "10":4660, "11":5500, "12":23300, "13":2880,
"14":23300, "15":2880, "16":3770, "17":4660, "18":5500, "19":23300, "20":2880,
"21":3770, "22":4660, "23":5500, "24":6440, "25":7330, "26":8220, "27":9110, 
"28":10000, "29":23300, "30":2880, "31":3770, "32":4660, "33":5500, "34":6440,
"35":7330, "36":8220, "37":9110, "38":10000, "39":23300, "40":2880, "41":3770,
"42":4660, "43":5500, "44":6440, "45":7330, "46":8220, "47":9110, "48":10000,
"49":23300, "50":0}

# Dict of dicts to access all cog dicts
bossbotDicts = {"FLUNKY":FLUNKY, "PENCILPUSHER":PENCILPUSHER, "YESMAN":YESMAN, "MICROMANAGER":MICROMANAGER, "DOWNSIZER":DOWNSIZER, "HEADHUNTER":HEADHUNTER, "CORPORATERAIDER":CORPORATERAIDER, "BIGCHEESE":BIGCHEESE}

# Dictionary of golf course stock options
golfStocks = {"three":764, "six":1874, "nine":3350}

# FUNCTION - Asks for the cog suit type and level, then stores them in variables
def askForCog():
     
     # Asks for cog type
     print("What cog are you on?")
     print("""(Enter one of the following: Flunky, Pencil Pusher, Yesman, Micromanager, Downsizer, Head Hunter, Corporate Raider, or Big Cheese.)""")
     bossSuit = input().upper()
     bossSuit = removeSpace(bossSuit)

     # If not a type, ask again
     if bossSuit not in bossbotTypes:
          print("Oops! That's not a Bossbot. Try typing a Bossbot.")
          bossSuit = input().upper()
          bossSuit = removeSpace(bossSuit)

     # Asks for cog level
     print("What level are you on?")
     bossLevel = input()

     # If not a number, ask again
     if bossLevel.isdigit() != True:
          print("Oops! Enter a number.")
          bossLevel = input()

     # If not in the specified Bossbot range (or negative), ask again
     if bossLevel not in bossbotDicts.get(bossSuit) or int(bossLevel) < 0:
          print("Oops! That's not a level for that cog. Try typing a correct level.")
          bossLevel = input()

     # Return a list containing the statistics of the suit desired
     return [bossSuit, bossLevel]

# FUNCTION - Prints the stock options that you need for the specified cog promotion
def printStocks(bossStats):

     # First check if the level is 50 and terminate if so
     if bossStats[0] == "50":
          print("You don't need anymore stock options, silly! Congrats on max bossbot!")
          return 0

     # Matches dictionary to cog type
     bossDict = bossbotDicts.get(bossStats[0])

     # Gets stock options from corresponding dictionary
     stocksNeeded = bossDict.get(bossStats[1])

     # Prints stock options
     print("For this cog promotion, you need " + str(stocksNeeded) + " stock options.")

     # Asks if you already have some options and prints how many you really need
     print("Do you already have some stock options? (Enter quantity. Enter 0 if you have none.)")
     stocksAcquired = input()
     while True:
          if stocksAcquired.isdigit() != True:
               print("That's not a number! Try entering a number.")
               stocksAcquired = input()
               continue
          elif int(stocksAcquired) > stocksNeeded or int(stocksAcquired) < 0:
               print("That can't be right. Try entering a number that makes sense, please!")
               stocksAcquired = input()
               continue
          elif stocksAcquired != "0":
               stocksRemaining = stocksNeeded - int(stocksAcquired)
               print("So, you actually need " + str(stocksRemaining) + " stock options.")
               break
          else:
               stocksRemaining = stocksNeeded
               break

     # Returns stock options needed for further calculation
     return stocksRemaining

# FUNCTION - Calculates how many Front Threes (ONLY) are needed
def frontThree(stocks):

     numFrontRaw = stocks / golfStocks.get("three")
     numFront = math.ceil(numFrontRaw)
     if numFront == 1:
          print("To do only Front Threes, you will need " + str(numFront) + " FRONT THREE to get all of your stock options.")
     else:
          print("To do only Front Threes, you will need " + str(numFront) + " FRONT THREES to get all of your stock options.")

# FUNCTION - Calculates how many Middle Sixes (ONLY) are needed
def middleSix(stocks):

     numMiddleRaw = stocks / golfStocks.get("six")
     numMiddle = math.ceil(numMiddleRaw)
     if numMiddle == 1:
          print("To do only Middle Sixes, you will need " + str(numMiddle) + " MIDDLE SIX to get all of your stock options.")
     else:
          print("To do only Middle Sixes, you will need " + str(numMiddle) + " MIDDLE SIXES to get all of your stock options.")

# FUNCTION - Calculates how many Back Nines (ONLY are needed)
def backNine(stocks):

     numBackRaw = stocks / golfStocks.get("nine")
     numBack = math.ceil(numBackRaw)
     if numBack == 1:
          print("To do only Back Nines, you will need " + str(numBack) + " BACK NINE to get all of your stock options.")
     else:
          print("To do only Back Nines, you will need " + str(numBack) + " BACK NINES to get all of your stock options.")

# FUNCTION - Calculates an ideal route for the least stock option waste
def idealGolf(stocks):

     # First asks if you want to consider Back Nines
     print("First, would you like to consider Back Nines in your calculation? They are very intense and dangerous, \nso it may be safer to omit them with a time sacrifice. (Y/N)")
     answer = input().upper()
     if answer == "Y":
          # With B9, calculates B9
          numBackRaw = stocks / golfStocks.get("nine")
          numBack = math.floor(numBackRaw)

          # Gets remainder for M6
          remainder_9 = stocks % golfStocks.get("nine")
          ratio_9 = remainder_9 / golfStocks.get("nine")
          if ratio_9 > 0.8: # 60% is arbitrary
               numBack = numBack + 1
               remainder_9 = remainder_9 - golfStocks.get("nine")
               if remainder_9 < 0:
                    remainder_9 = 0

          # Calculates M6
          numMiddle_9Raw = remainder_9 / golfStocks.get("six")
          numMiddle_9 = math.floor(numMiddle_9Raw)

          # Gets remainder for F3
          remainder_92 = remainder_9 % golfStocks.get("six")
          ratio_92 = remainder_92 / golfStocks.get("six")
          if ratio_92 > 0.7: # 70% is arbitrary
               numMiddle_9 = numMiddle_9 + 1
               remainder_92 = remainder_92 - golfStocks.get("six")
               if remainder_92 < 0:
                    remainder_92 = 0

          # Calculates F3 to finish
          numFront_9Raw = remainder_92 / golfStocks.get("three")
          numFront_9 = math.ceil(numFront_9Raw)

          # Prints ideal path
          print("Here is an ideal golf course path for you (With Back Nines).")
          if numBack == 1:
               backString = "BACK NINE"
          else:
               backString = "BACK NINES"

          if numMiddle_9 == 1:
               middleString = "MIDDLE SIX"
          else:
               middleString = "MIDDLE SIXES"

          if numFront_9 == 1:
               frontString = "FRONT THREE"
          else:
               frontString = "FRONT THREES"

          print("To get all your stock options, you will need " + str(numBack) + " " + backString + ", " + str(numMiddle_9) + " " + middleString + ", and " + str(numFront_9) + " " + frontString + ".")

          # Calculates more to implement buildings if short may be too long
          remainder_93 = remainder_92 % golfStocks.get("three")
          ratio_93 = remainder_93 / golfStocks.get("three")

          if ratio_93 < 0.2 and ratio_93 != 0: # 20% is arbitrary; seems to be excessive
               print("But because you only need " + str(remainder_93) + " more stock options, it may be more efficient to \ncomplete a cog building or two instead of one Front Three! The choice is up to you.")

     else:
          # Without B9, calculates M6
          numMiddleRaw = stocks / golfStocks.get("six")
          numMiddle = math.floor(numMiddleRaw)

          # Gets remainder for F3
          remainder = stocks % golfStocks.get("six")
          ratio = remainder / golfStocks.get("six")
          if ratio > 0.6: # 60% is arbitrary
               numMiddle = numMiddle + 1
               remainder = remainder - golfStocks.get("six")
               if remainder < 0:
                    remainder = 0

          # Calculates number of F3 to finish
          numFrontRaw = remainder / golfStocks.get("three")
          numFront = math.ceil(numFrontRaw)

          # Prints ideal path
          print("Here is an ideal gold course path for you (Without Back Nines).")
          if numMiddle == 1:
               middleString = "MIDDLE SIX"
          else:
               middleString = "MIDDLE SIXES"

          if numFront == 1:
               frontString = "FRONT THREE"
          else:
               frontString = "FRONT THREES"

          print("To get all your stock options, you will need " + str(numMiddle) + " " + middleString + " and " + str(numFront) + " " + frontString + ".")

          # Calculates more to implement buildings if short may be too long
          remainder2 = remainder % golfStocks.get("three")
          ratio2 = remainder2 / golfStocks.get("three")

          if ratio2 < 0.2 and ratio2 != 0: # 20% is arbitrary; seems to be excessive
               print("But because you only need " + str(remainder2) + " more stock options, it may be more efficient to \ncomplete a cog building or two instead of one Front Three! The choice is up to you.")
               