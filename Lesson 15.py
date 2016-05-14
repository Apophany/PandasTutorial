import Quandl
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
style.use('ggplot')

api_key = open("E:/python/QuandleApiKey.txt", "r").read()

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0


HPI_States = pd.read_pickle('fiftyStates.pickle')
HPI_Benchmark = pd.read_pickle('HPI_Benchmark.pickle')
SP500 = pd.read_pickle('SP500.pickle')
GDP = pd.read_pickle('gdp.pickle')
US_Unemployment = pd.read_pickle('US_Unemployment.pickle')
M30Y = pd.read_pickle('30YMortgage.pickle')

All_Data = HPI_Benchmark.join([M30Y, SP500, GDP, US_Unemployment])
All_Data.dropna(inplace=True)

All_Data = All_Data.pct_change()

All_Data.replace([np.inf, -np.inf], np.nan, inplace=True)
All_Data['US_HPI_Future'] = All_Data['US_HPI'].shift(-1)
All_Data.dropna(inplace=True)

All_Data['label'] = map(create_labels, All_Data['US_HPI'], All_Data['US_HPI_Future'])
print(All_Data.head())



All_Data['ma_apply_example'] = pd.rolling_apply(All_Data['M30Y'], 10, np.mean)
print(All_Data.tail())
