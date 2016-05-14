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

HPI_data = pd.read_pickle('fiftyStates.pickle')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A')

##figure = plt.figure()
##ax1 = plt.subplot2grid((1,1),(0,0))

##HPI_data['TX'].plot(ax=ax1)
##TX1yr.plot(color='k',ax=ax1)

HPI_data.fillna(value=-9999,inplace=True)

HPI_data[['TX','TX1yr']].plot()
print(HPI_data[['TX', 'TX1yr']])

plt.legend().remove()
plt.show()
