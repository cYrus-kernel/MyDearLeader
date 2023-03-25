def checkBullishHarami():
    if (tOpeningPrice > tMinusOneClosingPrice) & (tClosingPrice < tMinusOneOpeningPrice) & (tClosingPrice > tOpeningPrice) & (tClosingPrice - tOpeningPrice < (tMinusOneOpeningPrice - tMinusOneClosingPrice) * 0.7):
        return True
    else:
        return False
    
def checkBearishHarami():
    if (tOpeningPrice < tMinusOneClosingPrice) & (tClosingPrice > tMinusOneOpeningPrice) & (tClosingPrice < tOpeningPrice) & (tOpeningPrice - tClosingPrice < (tMinusOneClosingPrice - tMinusOneOpeningPrice) * 0.7):
       return True
    else:
        return False
    
def checkBullishEngulfing():
    if (tOpeningPrice < tMinusOneClosingPrice) & (tClosingPrice > tMinusOneOpeningPrice) & (tMinusOneClosingPrice < tMinusOneOpeningPrice):
        return True
    else:
        return False
    
def checkBearishEngulfing():
    if (tOpeningPrice > tMinusOneClosingPrice) & (tClosingPrice < tMinusOneOpeningPrice) & (tMinusOneClosingPrice > tMinusOneOpeningPrice):
        return True
    else:
        return False

def checkPiercingLine():
    if (tOpeningPrice < tMinusOneLowPrice) & (tClosingPrice > (tMinusOneOpeningPrice + tMinusOneClosingPrice) / 2):
        return True
    else:
        return False

def checkDarkCloudCover():
    if (tOpeningPrice > tMinusOneHighPrice) & (tClosingPrice < (tMinusOneOpeningPrice + tMinusOneClosingPrice) / 2):
        return True
    else:
        return False

def checkHomingPigeon():
    if (tOpeningPrice < tMinusOneOpeningPrice) & (tClosingPrice > tMinusOneClosingPrice) & (tClosingPrice < tOpeningPrice):
        return True
    else:
        return False

def checkDescendingHawk():
    if (tOpeningPrice > tMinusOneOpeningPrice) & (tClosingPrice < tMinusOneClosingPrice) & (tClosingPrice > tOpeningPrice):
        return True
    else:
        return False

tMinusOneOpeningPrice = int(input("Please type in the opening price at time t-1 : "))
tMinusOneClosingPrice = int(input("Please type in the closing price at time t-1 : "))
tMinusOneHighPrice = int(input("Please type in the high price at time t-1 : "))
tMinusOneLowPrice = int(input("Please type in the low price at time t-1 : "))

tOpeningPrice = int(input("Please type in the opening price at time t : "))
tClosingPrice = int(input("Please type in the closing price at time t : "))
tHighPrice = int(input("Please type in the high price at time t : "))
tLowPrice = int(input("Please type in the low price at time t: "))

# print(str(tMinusOneOpeningPrice) + str(tMinusOneClosingPrice) + str(tMinusOneHighPrice) + str(tMinusOneLowPrice))
# print(str(tOpeningPrice) + str(tClosingPrice) + str(tHighPrice) + str(tLowPrice))

if checkBullishHarami():
    print("Bullish Harami.")
elif checkBearishHarami():
    print("Bearish Harami.")
elif checkBullishEngulfing():
    print("Bullish Engulfing.")
elif checkBearishEngulfing():
    print("Bearish Engulfing.")
elif checkPiercingLine():
    print("Piercing Line.")
elif checkDarkCloudCover():
    print("Dark Cloud Cover.")
elif checkHomingPigeon():
    print("Homing Pigeon.")
elif checkDescendingHawk():
    print("Descending Hawk.")
else:
    print("None")