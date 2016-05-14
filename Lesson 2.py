import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,12,45,67,89,90],
             'Bounce_Rate':[12,34,56,21,45,78]}

webStatsDf = pd.DataFrame(web_stats)
webStatsDf.set_index('Day', inplace=True)

print(webStatsDf.head())


webStatsDf.plot()
plt.show()
