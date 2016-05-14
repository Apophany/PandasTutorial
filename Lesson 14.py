import Quandl
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

api_key = open("E:/python/QuandleApiKey.txt", "r").read()

def HPI_Benchmark():
    df = Quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.columns = ['United States']
    df["United States"] = (df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    df.rename(columns={'United States':'US_HPI'}, inplace=True)
    df.to_pickle('HPI_Benchmark.pickle')

def sp500_data():
    df = Quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
    df["Adjusted Close"] = (df["Adjusted Close"]-df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df=df.resample('M')
    df.rename(columns={'Adjusted Close':'sp500'}, inplace=True)
    df = df['sp500']
    df.to_pickle('SP500.pickle')

def gdp_data():
    df = Quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M')
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    df.to_pickle('gdp.pickle')

def us_unemployment():
    df = Quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df=df.resample('1D')
    df=df.resample('M')
    df.to_pickle('US_Unemployment.pickle')

def mortgage_30y():
    df = df = Quandl.get('FMAC/MORTG', trim_start='1975-01-01', authtoken=api_key)
    df.columns = ["M30Y"]
    df["M30Y"] = (df["M30Y"] - df["M30Y"][0]) / df["M30Y"][0] * 100.0
    df = df.resample('1D')
    df = df.resample('M')
    df.to_pickle('30YMortgage.pickle')

def initialLoad():
    HPI_Benchmark()
    sp500_data()
    gdp_data()
    us_unemployment()
    mortgage_30y()
    
# initialLoad()

HPI_States = pd.read_pickle('fiftyStates.pickle')
HPI_Benchmark = pd.read_pickle('HPI_Benchmark.pickle')
SP500 = pd.read_pickle('SP500.pickle')
GDP = pd.read_pickle('gdp.pickle')
US_Unemployment = pd.read_pickle('US_Unemployment.pickle')
M30Y = pd.read_pickle('30YMortgage.pickle')

All_Data = HPI_Benchmark.join([M30Y, SP500, GDP, US_Unemployment])

All_Data.dropna(inplace=True)

print(All_Data.corr())

All_Data.corr().plot()
plt.show()

