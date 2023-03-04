import numpy as np
import pandas as pd
import datetime as datetime

data = pd.read_csv('df2330_12to22.csv')

data['trend'] = np.where(data.Close.shift(-5) > data.Close, 1, 0)
print(data.isnull().sum())

print(data)
