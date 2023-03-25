import csv
import os

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
    
def detectPattern():
    if checkBullishHarami():
        print(day + " Bullish Harami.")
    elif checkBearishHarami():
        print(day + " Bearish Harami.")
    elif checkBullishEngulfing():
        print(day + " Bullish Engulfing.")
    elif checkBearishEngulfing():
        print(day + " Bearish Engulfing.")
    elif checkPiercingLine():
        print(day + " Piercing Line.")
    elif checkDarkCloudCover():
        print(day + " Dark Cloud Cover.")
    elif checkHomingPigeon():
        print(day + " Homing Pigeon.")
    elif checkDescendingHawk():
        print(day + " Descending Hawk.")
    else:
        print(day + " None")

# tMinusOneOpeningPrice = int(input("Please type in the opening price at time t-1 : "))
# tMinusOneClosingPrice = int(input("Please type in the closing price at time t-1 : "))
# tMinusOneHighPrice = int(input("Please type in the high price at time t-1 : "))
# tMinusOneLowPrice = int(input("Please type in the low price at time t-1 : "))

# tOpeningPrice = int(input("Please type in the opening price at time t : "))
# tClosingPrice = int(input("Please type in the closing price at time t : "))
# tHighPrice = int(input("Please type in the high price at time t : "))
# tLowPrice = int(input("Please type in the low price at time t: "))

# print(str(tMinusOneOpeningPrice) + str(tMinusOneClosingPrice) + str(tMinusOneHighPrice) + str(tMinusOneLowPrice))
# print(str(tOpeningPrice) + str(tClosingPrice) + str(tHighPrice) + str(tLowPrice))

# 開啟 CSV 檔案

current_dir = os.getcwd()
year = input("Please type in the year you wannna check : ")
file_path = os.path.join(current_dir, "source", "old", year + ".csv")

with open(file_path, newline='') as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

    # 以迴圈輸出每一列
    firstTime = 1
    firstDay = 1
    for row in rows:
        if(firstTime == 1):
            firstTime = 0
            continue
        else:
            if(firstDay == 1):
                tMinusOneOpeningPrice = float(row[1])
                tMinusOneHighPrice = float(row[2])
                tMinusOneLowPrice = float(row[3])
                tMinusOneClosingPrice = float(row[4])
                firstDay = 0
            else:
                tOpeningPrice = float(row[1])
                tHighPrice = float(row[2])
                tLowPrice = float(row[3])
                tClosingPrice = float(row[4])
                day = row[0]
                detectPattern()
                tMinusOneOpeningPrice = tOpeningPrice
                tMinusOneHighPrice = tHighPrice
                tMinusOneLowPrice = tLowPrice
                tMinusOneClosingPrice = tClosingPrice

# if checkBullishHarami():
#     print("Bullish Harami.")
# elif checkBearishHarami():
#     print("Bearish Harami.")
# elif checkBullishEngulfing():
#     print("Bullish Engulfing.")
# elif checkBearishEngulfing():
#     print("Bearish Engulfing.")
# elif checkPiercingLine():
#     print("Piercing Line.")
# elif checkDarkCloudCover():
#     print("Dark Cloud Cover.")
# elif checkHomingPigeon():
#     print("Homing Pigeon.")
# elif checkDescendingHawk():
#     print("Descending Hawk.")
# else:
#     print("None")