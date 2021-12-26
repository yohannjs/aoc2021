import numpy as np
import pandas as pd
from ast import literal_eval

rawDataDF = pd.read_csv('binary_report.csv')
# rawDataDF = pd.read_csv('test_data.csv')
bit_values = list(rawDataDF.columns)

oxyDF = rawDataDF.copy(deep=True)
co2DF = rawDataDF.copy(deep=True)

# print('Oxygen regeneration')
for val in bit_values:
    avg_value = oxyDF[val].mean()
    if avg_value == 0.5:
        avg_value += 0.1
    most_common = int(np.round(avg_value))
    oxyReducedDF = oxyDF.loc[oxyDF[val] == most_common]
    if oxyReducedDF.drop_duplicates(subset = bit_values).shape[0] == 1:
        oxy_bits = list(oxyReducedDF.drop_duplicates(subset = bit_values).values[0])
        break
    else:
        oxyDF = oxyReducedDF

oxy_string = '0b' + ''.join([str(integer) for integer in oxy_bits])
print(oxy_string)

# print('CO2 scrubbing')
for val in bit_values:
    # print('Iteration', val)
    avg_value = co2DF[val].mean()
    if avg_value == 0.5:
        avg_value += 0.1
    least_common = int(np.round(1 - avg_value))
    co2ReducedDF = co2DF.loc[co2DF[val] == least_common]
    if co2ReducedDF.drop_duplicates(subset = bit_values).shape[0] == 1:
        co2_bits = list(co2ReducedDF.drop_duplicates(subset = bit_values).values[0])
        break
    else:
        co2DF = co2ReducedDF

co2_string = '0b' + ''.join([str(integer) for integer in co2_bits])
print(co2_string)

print('Life support rating =', int(float(literal_eval(oxy_string))*float(literal_eval(co2_string))))
