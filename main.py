#This is the Quickest way to analyse any data file with(.csv) format 
# using pandas and ProfileReport of pandas_profiling
#It will give output in html format, if you want

import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('TB_data_dictionary_2020-06-03.csv')
print(df)
profile = ProfileReport(df)
profile.to_file(output_file="jay123.html")
