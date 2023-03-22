import pandas as pd 
import numpy as np

df2012 = pd.read_csv('2012.csv')
df2013 = pd.read_csv('2013.csv')
df2014 = pd.read_csv('2014.csv')
df2015 = pd.read_csv('2015.csv')
df2016 = pd.read_csv('2016.csv')
df2017 = pd.read_csv('2017.csv')
df2018 = pd.read_csv('2018.csv')
df2019 = pd.read_csv('2019.csv')
df2020 = pd.read_csv('2020.csv')
df2021 = pd.read_csv('2021.csv')
df2022 = pd.read_csv('2022.csv')


finaldata = pd.concat([df2012,df2013,df2014,df2015,df2016,df2017,df2018,df2019,df2020,df2021,df2022],axis=0,ignore_index=False)
print(finaldata)

finaldata.to_csv(r'C:\Users\mikai\GitHub\MyDearLeader\df2330_12to22.csv', encoding='utf-8',index=None)
