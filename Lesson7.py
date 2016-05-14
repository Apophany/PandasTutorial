import Quandl
import pickle
import pandas as pd

api_key = open("E:/python/QuandleApiKey.txt", "r").read()

def state_codes():
    return pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0][0][1:]


def save_intial_state():
    statesDf = pd.DataFrame()

    for state_code in state_codes():
        query = 'FMAC/HPI_' + str(state_code)
        print 'Asking for', query

        df = Quandl.get(query, authtoken=api_key)
        df.columns = [str(state_code)]
        print 'Got results', df.shape

        if statesDf.empty:
            statesDf = df
        else:
            statesDf = statesDf.join(df)

        print statesDf.head()


    statesDf.to_pickle('fiftyStates.pickle')

# save_intial_state()

HPI_data = pd.read_pickle('fiftyStates.pickle')
print(HPI_data)

    
    
