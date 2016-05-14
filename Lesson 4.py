import Quandl
import pandas as pd

stateCodes = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0][0][1:]

hpiDf = pd.DataFrame()

for stateCode in stateCodes:
    ticker = "FMAC/HPI_" + stateCode
    print(ticker)
    
    ##hpiDf = Quandl.get(ticker, authtoken=api_key)
