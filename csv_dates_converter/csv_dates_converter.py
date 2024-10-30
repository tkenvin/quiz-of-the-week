"""
Script to create a new CSV file containing a transformed version of the Quiz Of
The Week data. Specifically the transformation is to change how dates are
represented from separate columns ['day', 'month', 'year'] containing unpadded
integers where years are two digit e.g. [23,7,19] into ISO 8601 YYYY-MM-DD.
"""

import pandas as pd

# File names
INPUT_FILE_NAME = 'qotw-input.csv'
OUTPUT_FILE_NAME = 'qotw-output.csv'

# Existing columns
DAY = 'day'
MONTH = 'month'
YEAR = 'year'
NUMERATOR = 'numerator'
DENOMINATOR = 'denominator'
NOTES = 'notes'

# New column
DATE = 'date'

YEAR_OFFSET = 2000

data = pd.read_csv(INPUT_FILE_NAME)

data[YEAR] = data[YEAR] + YEAR_OFFSET
data[DATE] = pd.to_datetime(data[[DAY, MONTH, YEAR]])
data = data[[DATE, NUMERATOR, DENOMINATOR, NOTES]]

data.to_csv(OUTPUT_FILE_NAME, index=False)
