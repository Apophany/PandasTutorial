import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 6)

xomDf = web.DataReader("XOM", "yahoo", start, end)

xomDf.High.plot()
plt.legend()
plt.show()
