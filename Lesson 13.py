import Quandl
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

api_key = open("E:/python/QuandleApiKey.txt", "r").read()

def state_codes():
    return pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0][0][1:]

def HPI_benchmark_pct_change():
    df = Quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df.columns = ["United States"]
    df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100.0
    df.to_pickle('hpiBenchmarkPctChg.pickle')

def mortgage_30y():
    df = df = Quandl.get('FMAC/MORTG', trim_start='1975-01-01', authtoken=api_key)
    df.columns = ["M30Y"]
    df["M30Y"] = (df["M30Y"] - df["M30Y"][0]) / df["M30Y"][0] * 100.0
    df = df.resample('1D')
    df = df.resample('M')
    df.to_pickle('30YMortgage.pickle')

def save_intial_state():
    statesDf = pd.DataFrame()
    HPI_total_pct_change = pd.DataFrame()

    for state_code in state_codes():
        query = 'FMAC/HPI_' + str(state_code)
        print 'Asking for', query

        df = Quandl.get(query, authtoken=api_key)
        df.columns = [str(state_code)]

        total_pct = df
        total_pct[state_code] = (total_pct[state_code] - total_pct[state_code][0]) / total_pct[state_code][0] * 100
                                 
        print 'Got results', df.shape

        if statesDf.empty:
            statesDf = df
            HPI_total_pct_change = total_pct
        else:
            statesDf = statesDf.join(df)
            HPI_total_pct_change = HPI_total_pct_change.join(total_pct)

    statesDf.to_pickle('fiftyStates.pickle')
    HPI_total_pct_change.to_pickle('fiftyStatesTotalPctChg.pickle')

# save_intial_state()

# HPI_benchmark_pct_change()

# mortgage_30y()

HPI_data = pd.read_pickle('fiftyStates.pickle')
M30Y = pd.read_pickle('30YMortgage.pickle')
HPI_Bench = pd.read_pickle('hpiBenchmarkPctChg.pickle')

HPI = HPI_Bench.join(M30Y)

print(HPI.corr())

state_HPI = HPI_data.join(M30Y)
print(state_HPI.corr())

state_HPI.corr()['M30Y'].plot()
print(state_HPI.corr()['M30Y'].describe())

plt.show()
