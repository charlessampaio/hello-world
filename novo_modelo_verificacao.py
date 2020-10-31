
import pandas as pd
#import numpy as np
import seaborn as sns
#import scipy # factorial whorking just with 1.2 verson | pip install scipy==1.2 --upgrade
#import statsmodels
import statsmodels.api as sm
#from statsmodels.tsa.stattools import adfuller # https://www.statsmodels.org/dev/generated/statsmodels.tsa.stattools.adfuller.html


df = pd.read_csv('basemt5.csv')

symbol = 'CADCHF'

df = df[(df.symbol == symbol)]

df['Return'] = ((df['close'] / df['close'].shift(1)) - 1) * 100
df['open_Change'] = df['open'] - df['open'].shift(2)
df['high_Change'] = df['high'] - df['high'].shift(2)
df['low_Change'] = df['low'] - df['low'].shift(2)
df['close_Change'] = df['close'] - df['close'].shift(2)
df = df[df['close_Change'].notnull()]

y = df['Return']
x = df[['open_Change', 'high_Change', 'low_Change', 'close_Change']]

x = sm.add_constant(x)                          # Atribui variavel X para a regressao
result = sm.OLS(y, x).fit()                              # Executa a regressao

print(result.summary())
print('*' * 100)
print()
print(result.summary2())
print('*' * 100)
print()
print(result.params)