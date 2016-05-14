import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use('ggplot')


bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

bridgeDf = pd.DataFrame(bridge_height)
bridgeDf['STD'] = pd.rolling_std(bridgeDf['meters'], 2)
print(bridgeDf.describe())


df_std = bridgeDf.describe()['meters']['std']

bridgeDf = bridgeDf[ (bridgeDf['STD'] < df_std) ]

bridgeDf['meters'].plot()
plt.show()
