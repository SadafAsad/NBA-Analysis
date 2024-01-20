# import section
import pandas as pd
from nba_api.stats.static import teams
import sqlite3

# # ---------------------------------------------
# # How to create a dataframe from a dictionary
# # ---------------------------------------------
# # Notice key and value pairs
# # Keys are in simple string format and values are in array format
# dict_={'a':[11,21,31],'b':[12,22,32]}
# df=pd.DataFrame(dict_)
# print(f"type(df): \n{type(df)}\n")
# print(f"df.head(): \n{df.head()}\n")
# print(f"df.mean(): \n{df.mean()}\n")

# ----------------------------------------------------------------------------------
# Constructing a dictionary from an array of dictionaries
# with each key, value pair in the required format to later convert into dataframe
# key being a simple string and value an array
# ----------------------------------------------------------------------------------
def to_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# check what the returned data look like
nba_teams = teams.get_teams()
# print(nba_teams[0:3])

# nba api result to dataframe
dict_nba_teams=to_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_teams)
# print(df_teams.head())

# connecting to sqlite db
sql_connection = sqlite3.connect('nba.db')
# to convert pandas dataframe to a table in a sqlite db
df_teams.to_sql("NBATeams", sql_connection, if_exists='replace', index=False)

# query_stmt = "SELECT * FROM NBATeams"
# print(pd.read_sql(query_stmt, sql_connection))
