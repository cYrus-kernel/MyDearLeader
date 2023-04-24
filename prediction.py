import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
pd.options.mode.chained_assignment = None

stock_data = pd.read_csv('fulldata.csv')
stock_data["FutureOne"]= stock_data.Close.shift(-1)
stock_data["FutureThree"]= stock_data.Close.shift(-3)
stock_data["FutureFive"]= stock_data.Close.shift(-5)
modelOne = load_model('FutureOne.h5')
modelThree = load_model('FutureThree.h5')
modelFive = load_model('FutureFive.h5')

target = ['FutureOne']
features = ['Transaction','Open', 'High', 'Low','Close','ForeignNet','TrustNet','DealerNet']
df = stock_data[features + target]
split = int(df.shape[0] * 0.8)
df_test = df.iloc[split:, :].copy()

target_scaler = MinMaxScaler().fit(df[target])
features_scaler = MinMaxScaler().fit(df[features])
df_test[features] = features_scaler.transform(df_test[features])

# extract the input sequences and output values
sequence_length = 3
X_test, y_test = [], []

for i in range(sequence_length, df_test.shape[0]):
    X_test.append(df_test[features].iloc[i - sequence_length: i])
    y_test.append(df_test[target].iloc[i])

X_test, y_test = np.array(X_test), np.array(y_test)

y_predOne = modelOne.predict(X_test)
y_predOne = target_scaler.inverse_transform(y_predOne)
df['PredictedOne'] = np.nan
df['PredictedOne'].iloc[- y_predOne.shape[0]:] = y_predOne.flatten()

y_predThree = modelThree.predict(X_test)
y_predThree = target_scaler.inverse_transform(y_predThree)
df['PredictedThree'] = np.nan
df['PredictedThree'].iloc[- y_predThree.shape[0]:] = y_predThree.flatten()

y_predFive = modelFive.predict(X_test)
y_predFive = target_scaler.inverse_transform(y_predFive)
df['PredictedFive'] = np.nan
df['PredictedFive'].iloc[- y_predFive.shape[0]:] = y_predFive.flatten()

res=pd.concat([stock_data['DateTime'],df],axis=1)
test=res[['DateTime','Open','Close', 'PredictedOne','PredictedThree','PredictedFive']].dropna().reset_index(drop=True)
test.rename({'Close': 'Closing Price'}, axis=1, inplace=True)

plot=test.plot(x='DateTime',y=['Closing Price','PredictedOne'])
fig = plot.get_figure()
fig.savefig('PredictedOne.png')

plot2=test.plot(x='DateTime',y=['Closing Price','PredictedThree'])
fig2 = plot2.get_figure()
fig2.savefig('PredictedThree.png')

plot3=test.plot(x='DateTime',y=['Closing Price','PredictedFive'])
fig3 = plot3.get_figure()
fig3.savefig('PredictedFive.png')