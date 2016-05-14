import Quandl
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
from sklearn import svm, preprocessing, cross_validation
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

X = np.array(All_Data.drop(['label', 'US_HPI_Future'], 1))
X = preprocessing.scale(X)

y = np.array(All_Data['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

print(clf)
