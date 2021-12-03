import numpy as np
import pandas as pd

sonarDF = pd.DataFrame()
sonarDataSer = pd.read_csv('sonar_data.txt')
sonarDF['Data'] = sonarDataSer
sonarDF['Data_shifted'] = sonarDF['Data'].shift(1)
sonarDF['Count_inc'] = (sonarDF['Data'] - sonarDF['Data_shifted']) > 0
sonarDF['Count_inc'] = sonarDF['Count_inc'].astype(np.int64)
print(sonarDF.head())
print(sonarDF.tail())
print(sonarDF['Count_inc'].sum())