# import section
import pandas as pd
from nba_api.stats.static import teams
import sqlite3
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import leaguegamefinder

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

# ------------------
# Collecting Data
# ------------------
# check what the returned data look like
nba_teams = teams.get_teams()
# print(nba_teams[0:3])

# nba api result to dataframe
dict_nba_teams=to_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_teams)
# print(df_teams.head())

# --------------
# Storing Data
# --------------
DB_NAME = 'nba.db'
TABLE_NAME = "NBATeams"
# connecting to sqlite db
sql_connection = sqlite3.connect(DB_NAME)
# to convert pandas dataframe to a table in a sqlite db
df_teams.to_sql(TABLE_NAME, sql_connection, if_exists='replace', index=False)

# query_stmt = "SELECT * FROM NBATeams"
# print(pd.read_sql(query_stmt, sql_connection))

# ----------------
# Analyzing Data
# ----------------
query_stmt_1 = f"SELECT COUNT(*) AS teams_count, \
                    CASE \
                        WHEN year_founded<1946 THEN 'BEFORE-1945' \
                        WHEN year_founded between 1946 and 1964 THEN '1946-1964' \
                        WHEN year_founded between 1965 and 1980 THEN '1965-1980' \
                        WHEN year_founded between 1981 and 1996 THEN '1981-1996' \
                        ELSE '1997-NOW' \
                    END AS year_range \
                FROM {TABLE_NAME} year_grouped \
                GROUP BY year_range;"
# print(pd.read_sql(query_stmt_1, sql_connection))

# ----------------
# Visualizing Analysis
# ----------------
# res_df = pd.read_sql_query(query_stmt_1, sql_connection)

# fig, ax = plt.subplots()

# year_ranges = res_df['year_range'].array
# teams_count = res_df['teams_count'].array

# ax.bar(year_ranges, teams_count)
# ax.set_ylabel('Teams Count')
# ax.set_title('Number of NBA teams founded within year range')

# plt.show()

# TO BE CONTINUED
# ANOTHER SET OF DATA TO WORK WITH
# The parameter team_id_nullable is the unique ID for a team. 
# Under the hood, the NBA API is making a HTTP request.
# The information requested is provided and is transmitted via an HTTP response.
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612761)
gamefinder.get_json()
games = gamefinder.get_data_frames()[0]
print(games)
games.head()

games_home=games[games['MATCHUP']=='TOR vs. GSW']
games_home['PLUS_MINUS'].mean()

games_away=games[games['MATCHUP']=='TOR @ GSW']
games_away['PLUS_MINUS'].mean()

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
ax.set_title('Toronto Raptors (TOR) vs. Golden State Warriors(GSW)')
plt.show()
