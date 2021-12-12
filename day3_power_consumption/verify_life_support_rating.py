import numpy as np
import pandas as pd
from ast import literal_eval

rawDataDF = pd.read_csv('binary_report.csv')
bit_values = list(rawDataDF.columns)
avg_value_dict = {bit_val: rawDataDF[bit_val].mean() for bit_val in bit_values}
gamma_dict   = {bit_val: int(np.round(float(avg_value_dict[bit_val]))) for bit_val in bit_values}
epsilon_dict = {bit_val: int(np.round(float(1 - avg_value_dict[bit_val]))) for bit_val in bit_values}


reducedDF = rawDataDF.copy(deep=True)
for bit_val in bit_values:
    reduced_df = reducedDF.loc[reducedDF[bit_val] == gamma_dict[bit_val]]
    if reduced_df.shape[0] == 1:
        break
    else:
        del reducedDF
        reducedDF = reduced_df

oxy_rating_string = '0b' + ''.join(map(str, list(reduced_df.values[0])))

del reducedDF, reduced_df
reducedDF = rawDataDF.copy(deep=True)
for bit_val in bit_values:
    reduced_df = reducedDF.loc[reducedDF[bit_val] == epsilon_dict[bit_val]]
    if reduced_df.shape[0] == 1:
        break
    else:
        del reducedDF
        reducedDF = reduced_df

co2_rating_string = '0b' + ''.join(map(str, list(reduced_df.values[0])))

print(float(literal_eval(oxy_rating_string)))
print(float(literal_eval(co2_rating_string)))
print('Life support rating =', int(float(literal_eval(oxy_rating_string))*float(literal_eval(co2_rating_string))))
