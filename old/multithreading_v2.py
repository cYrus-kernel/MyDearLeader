import pandas as pd
import numpy as np
import json
import requests
import concurrent.futures
import time
import xlwings as xw 

def Get_StockPrice(Symbol,Date):
    
    url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={Date}&stockNo={Symbol}' #股票的網址

    data = requests.get(url).text
    json_data = json.loads(data)

    Stock_data = json_data['data']

    StockPrice = pd.DataFrame(Stock_data, columns = ['Date','Volume','Volume_Cash','Open','High','Low','Close','Change','Order'])

    StockPrice['Date'] = StockPrice['Date'].str.replace('/','').astype(int) + 19110000
    StockPrice['Date'] = pd.to_datetime(StockPrice['Date'].astype(str))
    StockPrice['Volume'] = StockPrice['Volume'].str.replace(',','').astype(float)/1000
    StockPrice['Volume_Cash'] = StockPrice['Volume_Cash'].str.replace(',','').astype(float)
    StockPrice['Order'] = StockPrice['Order'].str.replace(',','').astype(float)

    StockPrice['Open'] = StockPrice['Open'].str.replace(',','').astype(float)
    StockPrice['High'] = StockPrice['High'].str.replace(',','').astype(float)
    StockPrice['Low'] = StockPrice['Low'].str.replace(',','').astype(float)
    StockPrice['Close'] = StockPrice['Close'].str.replace(',','').astype(float)

    StockPrice = StockPrice.set_index('Date', drop = True)


    StockPrice = StockPrice[['Open','High','Low','Close','Volume']]
    #xw.view(StockPrice)
    return StockPrice

        
def getdata():
    yearstart = int(input("請輸入起始年分:  "))
    yearend = int(input("請輸入截止年分:  "))
    symbol =str(input("請輸入股票編號:  "))
    monthstart =1
    monthend =12
    start_time = time.time()  # 開始時間
    dates=[]
    symbols=[]

    for year in range(yearstart,yearend+1):
        for month in range(monthstart,monthend+1):
            yearstr=str(year)
            if month>9:
                mon=str(month)
                date=yearstr+mon+"01"
            else:
                mon=str(month)
                date=yearstr+"0"+mon+"01"
            dates.append(date)
            symbols.append(symbol)
    print("multithreading...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        try:
            result=list(executor.map(Get_StockPrice,symbols,dates))
        except:
            print("Something is wrong")
    
    return result
    
mydata=getdata()
finaldata = pd.concat(mydata)
print(finaldata)

finaldata.to_csv(r'C:\Users\mikai\GitHub\MyDearLeader\2330.csv', encoding='utf-8')