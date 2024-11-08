"""
Script to analyse the Quiz of the Week data from the CSV. Specifically it
creates a scatter plot with all the results and also a statistical analysis of
each denominator. 
"""

import pandas as pd
from matplotlib import pyplot as plt

# File name
INPUT_FILE_NAME = 'qotw.csv'

# Existing columns
DATE = 'date'
NUMERATOR = 'numerator'
DENOMINATOR = 'denominator'

# New column
WEIGHTED = 'weighted'

data = pd.read_csv(INPUT_FILE_NAME)
data[WEIGHTED] = data[NUMERATOR]/data[DENOMINATOR]
data[DATE] = pd.to_datetime(data[DATE], format='%Y-%m-%d')

groups = data.groupby(by=DENOMINATOR)

plt.figure(figsize=(50, 20))
plt.scatter(data[DATE], data[WEIGHTED])
cols = groups.indices
analysis = pd.DataFrame()
for i in cols:
    group = groups.get_group(i)
    analysis[i] = group[NUMERATOR].describe()
    plt.scatter(group[DATE], group[NUMERATOR])

plt.savefig('./scatter.png')

analysis.to_csv('./analysistable.csv')
