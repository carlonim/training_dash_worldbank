import pandas as pd
from pandas_datareader import wb

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = wb.get_indicators()[['id', 'name']]
df = df[df.name == 'Carbon dioxide (CO2) emissions (total) excluding LULUCF (Mt CO2e)']
print(df)