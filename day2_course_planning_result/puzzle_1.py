import numpy as np
import pandas as pd

sonarCourseDF = pd.read_csv('puzzle_input.txt')
steps = []
for idx, row in sonarCourseDF.iterrows():
    if(row['Direction'] == 'up'):
        steps.append(-sonarCourseDF['Nr_steps'][idx])
    else:
        steps.append(sonarCourseDF['Nr_steps'][idx])
sonarCourseDF['Steps'] = steps

hor_pos = sonarCourseDF.iloc[np.where(sonarCourseDF['Direction'] == 'forward')]['Steps'].sum()
dep_pos = sonarCourseDF.iloc[np.where(sonarCourseDF['Direction'] == 'down')]['Steps'].sum() + sonarCourseDF.iloc[np.where(sonarCourseDF['Direction'] == 'up')]['Steps'].sum()

print(hor_pos*dep_pos)