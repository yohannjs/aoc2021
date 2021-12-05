import numpy as np
import pandas as pd

sonarCourseDF = pd.read_csv('puzzle_input.txt')
aim = 0
horizontal_position = 0
depth = 0
for idx, row in sonarCourseDF.iterrows():
    if(row['Direction'] == 'up'):
        aim += -row['Nr_steps']
    elif(row['Direction'] == 'down'):
        aim += row['Nr_steps']
    else:
        horizontal_position += row['Nr_steps']
        depth += aim*row['Nr_steps']

print('Product:', depth*horizontal_position)