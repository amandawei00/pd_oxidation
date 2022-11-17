import numpy as np
import csv
import pandas as pd

df1 = pd.read_csv('221031_Pd111_001.txt', header=None, delimiter=',', comment='#')
df2 = pd.read_csv('221031_Pd111_002.txt', header=None, delimiter=',', comment='#')
df3 = pd.read_csv('221031_Pd111_003.txt', header=None, delimiter=',', comment='#')
df4 = pd.read_csv('221031_Pd111_004.txt', header=None, delimiter=',', comment='#')
df5 = pd.read_csv('221031_Pd111_005.txt', header=None, delimiter=',', comment='#')

df1.columns = ['t1', 'N', 'O', 'CH4', 'Ar', 'CO2', 'H2O', '']
df2.columns = ['t2', 'N', 'O', 'CH4', 'Ar', 'CO2', 'H2O', '']
df3.columns = ['t3', 'N', 'O', 'CH4', 'Ar', 'CO2', 'H2O', '']
df4.columns = ['t4', 'N', 'O', 'CH4', 'Ar', 'CO2', 'H2O', '']
df5.columns = ['t5', 'N', 'O', 'CH4', 'Ar', 'CO2', 'H2O', '']

t1 = df1['t1']
p1 = df1['CH4']

t2 = df2['t2']
p2 = df2['CH4']

t3 = df3['t3']
p3 = df3['CH4']

t4 = df4['t4']
p4 = df4['CH4']

t5 = df5['t5']
p5 = df5['CH4']

out1 = pd.concat([t1, p1], ignore_index=True, axis=1)
out2 = pd.concat([t2, p2], ignore_index=True, axis=1)
out3 = pd.concat([t3, p3], ignore_index=True, axis=1)
out4 = pd.concat([t4, p4], ignore_index=True, axis=1)
out5 = pd.concat([t5, p5], ignore_index=True, axis=1)

out1.columns = ['t', 'p']
out2.columns = ['t', 'p']
out3.columns = ['t', 'p']
out4.columns = ['t', 'p']
out5.columns = ['t', 'p']

out1.to_csv('dat1_ox5.csv', sep='\t', index=None, header=True, float_format='%g')
out2.to_csv('dat2_ox10.csv', sep='\t', index=None, header=True, float_format='%g')
out3.to_csv('dat3_ox20.csv', sep='\t', index=None, header=True, float_format='%g')
out4.to_csv('dat4_ox40.csv', sep='\t', index=None, header=True, float_format='%g')
out5.to_csv('dat5_ox80.csv', sep='\t', index=None, header=True, float_format='%g')
