# MAIN

# Import other categories of functions
import sellbot
import cashbot
import lawbot
import bossbot
import otherFuncs

# Introduction
print()
print(" ** TTR COG PROMOTION BOT **")
print("This bot is designed to help any Toon who is trying to level up their cog suits efficiently.")
print("Say goodbye to your massive, time-devouring spreadsheets of calculations.  This tool is fast!")
print("Thank you for using this calculator and good luck with your journey to max laff!")
print("Using only your cog suit and level, I will determine different combinations \nof cog facilities to complete.")
print()

# Asking for cog type desired for calculation
print("What cog type would you like to calculate for? \n(Enter one of the following: Sellbot, Cashbot, Lawbot, Bossbot)")
print('(Enter "Nevermind" to exit.)')
cogType = input().lower()

# -------------------------------------------------------------------------------------------------------------------------
# Determines what function to use for calculation based on cog type
while True:

    # SELLBOT
    if cogType == "sellbot":

        # Using Sellbot functions to find cog type, level, and merits required
        sellStats = sellbot.askForCog()
        meritsRemaining = sellbot.printMerits(sellStats)

        # If not level 50, will continue calculations
        if meritsRemaining != 0:   # meritsNeeded is set to 0 in the printMerits function if level is 50
            
            # Asks what kind of path you want
            print("If you typically play for shorter periods of time, doing short factories may be the most effective.")
            print("If you play for long stretches and aren't afraid of commitment, long factories can be an easy grind.")
            print("If you, for some reason, like side factories, which only provide a little more than shorts, I can calculate that too.")
            print("I can also determine a combination of these to create a plan that reduces wasted time and merits!")
            print("Which would you like? (Enter one of the following: Short, Long, Side, or Ideal)")
            factChoice = input().upper()
            while True:
                if factChoice == "SHORT":
                    sellbot.shortFact(meritsRemaining)
            
                elif factChoice == "LONG":
                    sellbot.longFact(meritsRemaining)
                    
                elif factChoice == "SIDE":
                    sellbot.sideFact(meritsRemaining)
                    
                elif factChoice == "IDEAL":
                    sellbot.idealFact(meritsRemaining)
                    
                else:
                    print('Oops! Try typing a factory type or "ideal."')
                    factChoice = input().upper()
                    continue
            
                #  Ask if user would like a different path calculation with same suit
                print("Would you like to see another path for the same suit? (Y/N)")
                answer = input().upper()
                if answer == "Y":
                    print("Which would you like? (Enter one of the following: Short, Long, Side, or Ideal")
                    factChoice = input().upper()
                    continue
                else:
                    break 


        # Ask for another calculation after a previous one or after asking about level 50
        # (Repeats if yes, exits if no)
        print("Would you like to make a different suit calculation? (Y/N)")
        answer = input().upper()
        if answer == "Y":
            print("What cog type would you like to calculate for? \n(Enter one of the following: Sellbot, Cashbot, Lawbot, Bossbot)")
            cogType = input().lower()
            continue
        else:
            print("Have fun in ToonTown! Good luck and see you later!")
            break
        
    # -------------------------------------------------------------------------------------------------------------------------    
    # CASHBOT
    elif cogType == "cashbot":

        # Using Cashbot functions to find cog type, level, and cogbucks required
        cashStats = cashbot.askForCog()
        cogbucksRemaining = cashbot.printCogbucks(cashStats)

        # If not level 50, will continue calculations
        if cogbucksRemaining != 0:   # cogbucksNeeded is set to 0 in the printCogbucks function if level is 50
            
            # Asks what kind of path you want
            print("All Cashbot mints are a bigger time commitment than Sellbot factories, but still manageable with 3 different options.")
            print("If you want the minimum time commitment and difficulty, do a Coin Mint.")
            print("If you want a little more Cogbucks than a Coin Mint, Dollar Mints are very doable. Make sure you have at least 66 Laff!")
            print("If you want maximum XP and maximum Cogbucks, go for a Bullion Mint. I hope you have a lot of strong Toons and at least 71 Laff (But hopefully more).")
            print("I can also determine a combination of these to create a plan that reduces wasted time and Cogbucks!")
            print("Beware: Each Mint does NOT have a guaranteed number of Cogbucks as the cog numbers vary. But I will give you a range!")
            print("Which would you like? (Enter one of the following: Coin, Dollar, Bullion, or Ideal)")
            mintChoice = input().upper()
            while True:
                if mintChoice == "COIN":
                    cashbot.coinMint(cogbucksRemaining)
            
                elif mintChoice == "DOLLAR":
                    cashbot.dollarMint(cogbucksRemaining)
                    
                elif mintChoice == "BULLION":
                    cashbot.bullionMint(cogbucksRemaining)
                    
                elif mintChoice == "IDEAL":
                    cashbot.idealMint(cogbucksRemaining)
                    
                else:
                    print('Oops! Try typing a mint type or "ideal."')
                    mintChoice = input().upper()
                    continue
            
                #  Ask if user would like a different path calculation with same suit
                print("Would you like to see another path for the same suit? (Y/N)")
                answer = input().upper()
                if answer == "Y":
                    print("Which would you like? (Enter one of the following: Coin, Dollar, Bullion, or Ideal")
                    mintChoice = input().upper()
                    continue
                else:
                    break 

        # Ask for another calculation after a previous one or after asking about level 50
        # (Repeats if yes, exits if no)
        print("Would you like to make a different suit calculation? (Y/N)")
        answer = input().upper()
        if answer == "Y":
            print("What cog type would you like to calculate for? \n(Enter one of the following: Sellbot, Cashbot, Lawbot, Bossbot)")
            cogType = input().lower()
            continue
        else:
            print("Have fun in ToonTown! Good luck and see you later!")
            break

    # -------------------------------------------------------------------------------------------------------------------------
    # LAWBOT
    elif cogType == "lawbot":

        # Using Lawbot functions to find cog type, level, and jury notices required
        lawStats = lawbot.askForCog()
        noticesRemaining = lawbot.printNotices(lawStats)

        # If not level 50, will continue calculations
        if noticesRemaining != 0:   # noticesNeeded is set to 0 in the printNotices function if level is 50
            
            # Asks what kind of path you want
            print("All DA Offices are a grind. But Office A is the least time consuming and good for smaller promotions.")
            print("If you need more than an Office A, then try an Office B.")
            print("If you, for some reason, use Office C (Which is uncommon), I can calculate that too.")
            print("If you need the M A X I M U M to really crank out those big promos, I can bring you to Office D.")
            print("I can also determine a combination of these to create a plan that reduces wasted time and jury notices!")
            print("Which would you like? (Enter one of the following: A, B, C, D, or Ideal)")
            offChoice = input().upper()
            while True:
                if offChoice == "A":
                    lawbot.officeA(noticesRemaining)
            
                elif offChoice == "B":
                    lawbot.officeB(noticesRemaining)
                    
                elif offChoice == "C":
                    lawbot.officeC(noticesRemaining)

                elif offChoice == "D":
                    lawbot.officeD(noticesRemaining)
                    
                elif offChoice == "IDEAL":
                    lawbot.idealOff(noticesRemaining)
                    
                else:
                    print('Oops! Try typing a DA Office type or "ideal."')
                    offChoice = input().upper()
                    continue
            
                #  Ask if user would like a different path calculation with same suit
                print("Would you like to see another path for the same suit? (Y/N)")
                answer = input().upper()
                if answer == "Y":
                    print("Which would you like? (Enter one of the following: A, B, C, D, or Ideal")
                    offChoice = input().upper()
                    continue
                else:
                    break 

        # Ask for another calculation after a previous one or after asking about level 50
        # (Repeats if yes, exits if no)
        print("Would you like to make a different suit calculation? (Y/N)")
        answer = input().upper()
        if answer == "Y":
            print("What cog type would you like to calculate for? \n(Enter one of the following: Sellbot, Cashbot, Lawbot, Bossbot)")
            cogType = input().lower()
            continue
        else:
            print("Have fun in ToonTown! Good luck and see you later!")
            break
    
    # -------------------------------------------------------------------------------------------------------------------------
    # BOSSBOT
    elif cogType == "bossbot":
        # Using Bossbot functions to find cog type, level, and stock options required
        bossStats = bossbot.askForCog()
        stocksRemaining = bossbot.printStocks(bossStats)

        # If not level 50, will continue calculations
        if stocksRemaining != 0:   # stocksNeeded is set to 0 in the printStocks function if level is 50
            
            # Asks what kind of path you want
            print("All golf courses are a grind. But a Front Three is the least time consuming and good for smaller promotions.")
            print("If you need more than a Front Three, then go for the Middle Six.")
            print("If you need BIG stock options to really crank out those big promos, I can bring you to the notorious, hour-consuming Back Nine.")
            print("I can also determine a combination of these to create a plan that reduces wasted time and stock options!")
            print("Which would you like? (Enter one of the following: Three (3), Six (6), Nine (9), or Ideal)")
            golfChoice = input().upper()
            while True:
                if golfChoice == "THREE" or golfChoice == "3":
                    bossbot.frontThree(stocksRemaining)
            
                elif golfChoice == "SIX" or golfChoice == "6":
                    bossbot.middleSix(stocksRemaining)
                    
                elif golfChoice == "NINE" or golfChoice == "9":
                    bossbot.backNine(stocksRemaining)
                    
                elif golfChoice == "IDEAL":
                    bossbot.idealGolf(stocksRemaining)
                    
                else:
                    print('Oops! Try typing a golf course type or "ideal."')
                    golfChoice = input().upper()
                    continue
            
                #  Ask if user would like a different path calculation with same suit
                print("Would you like to see another path for the same suit? (Y/N)")
                answer = input().upper()
                if answer == "Y":
                    print("Which would you like? (Enter one of the following: A, B, C, D, or Ideal")
                    golfChoice = input().upper()
                    continue
                else:
                    break 

        # Ask for another calculation after a previous one or after asking about level 50
        # (Repeats if yes, exits if no)
        print("Would you like to make a different suit calculation? (Y/N)")
        answer = input().upper()
        if answer == "Y":
            print("What cog type would you like to calculate for? \n(Enter one of the following: Sellbot, Cashbot, Lawbot, Bossbot)")
            cogType = input().lower()
            continue
        else:
            print("Have fun in ToonTown! Good luck and see you later!")
            break

    # -------------------------------------------------------------------------------------------------------------------------
    # EXIT
    elif cogType == "nevermind":
        print("Have fun in ToonTown! Good luck and see you later!")
        break

    # INVALID
    else:
        print("Oops! Try typing a cog type.")
        cogType = input().lower()
        continue   