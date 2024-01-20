# ---------------------------------------------
# How to create a dataframe from a dictionary
# ---------------------------------------------
import pandas as pd
# Notice key and value pairs
# Keys are in simple string format and values are in array format
dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
print(f"type(df): \n{type(df)}\n")
print(f"df.head(): \n{df.head()}\n")
print(f"df.mean(): \n{df.mean()}\n")


