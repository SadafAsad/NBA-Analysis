# ---------------------------------------------
# How to create a dataframe from a dictionary
# ---------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
# Notice key and value pairs
# Keys are in simple string format and values are in array format
dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
type(df)
df.head()
df.mean()


