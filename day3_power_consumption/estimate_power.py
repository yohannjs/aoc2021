import numpy as np
import pandas as pd
from ast import literal_eval

rawDataDF = pd.read_csv('binary_report.csv')
bit_values = list(rawDataDF.columns)
avg_value_dict = {bit_value: rawDataDF[bit_value].mean() for bit_value in bit_values}
list_gamma   = [int(np.round(float(avg_value_dict[bit_value]))) for bit_value in bit_values]
list_epsilon = [int(np.round(float(1 - avg_value_dict[bit_value]))) for bit_value in bit_values]

gamma_string   = '0b' + ''.join(map(str, list_gamma))
epsilon_string = '0b' + ''.join(map(str, list_epsilon))
print(gamma_string)
print(epsilon_string)

print(float(literal_eval(gamma_string)))
print(float(literal_eval(epsilon_string)))

print('Power consumption =', int(float(literal_eval(gamma_string))*float(literal_eval(epsilon_string))))
