#Generate a cross tab (similar to pivot table)
# pip install openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data from excel
df = pd.read_excel('sample_1.xlsx')

# print top rows
print("Data snapshot")
print(df.head())
print()

# create a cross tab on Region and Type
ct1=pd.crosstab(df.Region, df.Type)
# This is the same as:
# pd.crosstab(index = df.Region, columns = df.Type)
# default aggregation is counts

print("Crosstab:  Region vs Type")
print(ct1)
print()
print('\n1111111111111111111111111111111')
input('Hit enter to proceed')
print()

# use mean as aggregation
ct2=pd.crosstab(index = df.Region, columns = df.Type, values = df.Sales, aggfunc = 'mean')
print("Crosstab  Region vs Type Aggregation on Sales")
print(ct2)
print()
print('\n222222222222222222222222222')
input('Hit enter to proceed')
print()

# multi index cross tab
# cross tab Region and Quarters  vs Type
ct3 =pd.crosstab([df.Region, df.Date.dt.quarter], df.Type)
print("Crosstab  Region vs Type indexed on quarters")
print(ct3)
print()
print('\n333333333333333333333333333333333333')
input('Hit enter to proceed')
print()

# modifying the Labels
ct4=pd.crosstab([df.Region, df.Date.dt.quarter], df.Type, rownames=['Region', 'Quarter'])
print("Crosstab  Region vs Type indexed on quarters with changed Labels")
print(ct4)
print()
print('\n4444444444444444444444444444444444444')
input('Hit enter to proceed')
print()

# cross tab with index for type
ct5=pd.crosstab(df.Region, [df.Type, df.Date.dt.quarter])
print("Crosstab  Region vs Type indexed on Type")
print(ct5)
print()
print('\n55555555555555555555555555555555555555')
input('Hit enter to proceed')
print()


# Adding totals to Cross tabs. Set margins = True
ct7 = pd.crosstab(df.Region, df.Type, margins=True, margins_name='Sub Totals')
print("Crosstab  Region vs Type Normalised with Totals")
print(ct7)
print()
print('\n666666666666666666666666666666666666')
input('Hit enter to proceed')
print()

import seaborn as sns
# plotting crosstab details as stacked bar chart
pd.crosstab(df.Region, df.Type, normalize='index').plot.bar(stacked=True)
plt.show()

# heat map to visualize 
sns.heatmap( pd.crosstab(df.Region, df.Type, values=df.Sales , aggfunc ='mean'))
plt.show()

print("Job Done")

