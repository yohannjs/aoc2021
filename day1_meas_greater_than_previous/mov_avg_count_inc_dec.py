import numpy as np
import pandas as pd

sonarDF = pd.read_csv('sonar_data.txt')

def compute_inc_sum(sonarDDF):
    sonarDataDF = sonarDDF.copy()
    sonarDataDF['Data_shifted'] = sonarDataDF['Data'].shift(1)
    sonarDataDF['Count_inc'] = (sonarDataDF['Data'] - sonarDataDF['Data_shifted']) > 0
    sonarDataDF['Count_inc'] = sonarDataDF['Count_inc'].astype(np.int64)
    return  sonarDataDF['Count_inc'].sum()

raw_inc_sum = compute_inc_sum(sonarDF)

sonarDF['Data_shifted1'] = sonarDF['Data'].shift(-1)
sonarDF['Data_shifted2'] = sonarDF['Data'].shift(-2)
sonarDF['Data_sum'] = sonarDF['Data'] + sonarDF['Data_shifted1'] + sonarDF['Data_shifted2']
sonarAvgDF = pd.DataFrame()
sonarAvgDF['Data'] = sonarDF['Data_sum']
sonarAvgDF.dropna(inplace=True)
print(sonarAvgDF.tail())
avg_sum = compute_inc_sum(sonarAvgDF)
print("Average sum", avg_sum)
