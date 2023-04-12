import random

'''
This is a Casino Game a player bids the amount to loss if he predicts that the new level of the Casino coin 
will rise above a certain level of value. 
'''
def randomGet():
    x = random.randint(0 , 7)
    return x
def loadGame():
    currencyUsed = int(input("Choose a currency :\n  1. USD\n  2. EUR\n  3. KSH \nInput a number corresponding to currency below : \n"))
    if currencyUsed == 1:
        currencyUsed = "$"
    elif currencyUsed == 2:
        currencyUsed = "euro."
    elif currencyUsed == 3:
        currencyUsed = "Ksh."
    else:
        raise ValueError("Sorry! Invalid input.")
    deposit = float(input("Enter the Amount to deposit : \n"))
    bid = float(input("Enter the amount to bid: \n"))
    newAmount = deposit - bid
    level = int(input("Enter the level : \n"))
    x = randomGet()
    print("Level Achieved is : ",x )
    if x > level:
        pointGained = (x-level) + 1
        amountGained = pointGained * level
        accountBalance = amountGained + deposit
        print("Congratulations \n Points Gained : ",pointGained,"points\n")
        print("Your profit is ",currencyUsed, amountGained)
        print("new account balance : ", currencyUsed, accountBalance)
        
    else:
        pointGained = 0
        amountGained = 0
        accountBalance = newAmount
        print("Sorry you have lost \n please try again.")
        print("new account balance : ", currencyUsed, accountBalance)
        

def main():
    
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,💖️,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
    print(",,,,,,,,,,,,,,,,,,,,,,,,,💖️💖️,,,,,,,,,,,,,,,,,,,,,,,,,\n")
    print("\t\tHi there! 👋️, \n\twelcome to Silgho Casino ltd.\n")
    print(",,,,,,,,,,,,,,,,,,,,,,,,💖️💖️💖️,,,,,,,,,,,,,,,,,,,,,,,,\n")

    print("Here you can become a multimillionaire by guessing new levels ")
    loadGame()
    
main()