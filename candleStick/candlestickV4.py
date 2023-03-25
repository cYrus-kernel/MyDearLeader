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
        rowWithBullishHarami = row + ["Bullish Harami"]
        csvwriter.writerow(rowWithBullishHarami)
        print(day + " Bullish Harami.")
    elif checkBearishHarami():
        rowWithBearishHarami = row + ["Bearish Harami"]
        csvwriter.writerow(rowWithBearishHarami)
        print(day + " Bearish Harami.")
    elif checkBullishEngulfing():
        rowWithBullishEngulfing = row + ["Bullish Engulfing"]
        csvwriter.writerow(rowWithBullishEngulfing)
        print(day + " Bullish Engulfing.")
    elif checkBearishEngulfing():
        rowWithBearishEngulfing = row + ["Bearish Engulfing"]
        csvwriter.writerow(rowWithBearishEngulfing)
        print(day + " Bearish Engulfing.")
    elif checkPiercingLine():
        rowWithPiercingLine = row + ["Piercing Line"]
        csvwriter.writerow(rowWithPiercingLine)
        print(day + " Piercing Line.")
    elif checkDarkCloudCover():
        rowWithDarkCloudCover = row + ["Dark Cloud Cover"]
        csvwriter.writerow(rowWithDarkCloudCover)
        print(day + " Dark Cloud Cover.")
    elif checkHomingPigeon():
        rowWithHomingPigeon = row + ["Homing Pigeon"]
        csvwriter.writerow(rowWithHomingPigeon)
        print(day + " Homing Pigeon.")
    elif checkDescendingHawk():
        rowWithDescendingHawk = row + ["Descending Hawk"]
        csvwriter.writerow(rowWithDescendingHawk)
        print(day + " Descending Hawk.")
    else:
        rowWithNone = row + ["None"]
        csvwriter.writerow(rowWithNone)
        print(day + " None")

# get file path
current_dir = os.getcwd()
start_year = input("Please type in the starting year you wannna check : ")
finish_year = input("Please type in the finishing year you wannna check : ")

# Open the file for writing
outputFileName = "output.csv"
with open(outputFileName, 'w', newline='') as csvfileV2:

    # Create a CSV writer object
    csvwriter = csv.writer(csvfileV2)

    for year in range(int(start_year), int(finish_year) + 1):
        # 開啟 CSV 檔案
        file_path = os.path.join(current_dir, "source", "old", str(year) + ".csv")
        with open(file_path, newline='') as csvfile:

            # 讀取 CSV 檔案內容
            rows = csv.reader(csvfile)

            # 以迴圈輸出每一列
            firstTime = 1
            firstDay = 1
            for row in rows:
                if(firstTime == 1):
                    firstTime = 0
                    rowWithPattern = row + ["Pattern"]
                    csvwriter.writerow(rowWithPattern)
                    continue
                else:
                    if(firstDay == 1):
                        tMinusOneOpeningPrice = float(row[1])
                        tMinusOneHighPrice = float(row[2])
                        tMinusOneLowPrice = float(row[3])
                        tMinusOneClosingPrice = float(row[4])
                        firstDay = 0
                        rowFirstDay = row + ["None"]
                        csvwriter.writerow(rowFirstDay)
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