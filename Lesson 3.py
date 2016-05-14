import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

nyHousingIndexDf = pd.read_csv('E:\Python\Data Analysis - Pandas\ZILL-Z10027_A.csv')
nyHousingIndexDf.set_index('Date', inplace=True)

nyHousingIndexDf.rename(columns={'Value':'House_Price'}, inplace=True)

nyHousingIndexDf.plot()
plt.show()
