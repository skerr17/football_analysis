# in this program we will split define a function that will 
# isolate a given team into its own dataframe

# import the pandas library
import pandas as pd
# import the os library
import os

# import the kagglehub library
# This library is used to download datasets from Kaggle
import kagglehub

# import impport_dataset to get the dataframe of football results
from import_dataset import football_results_df



def isolate_team(team_name):
    """
    This function takes a team name as input and returns a dataframe,
    containing only the matches played by that team.
    """
    # filter the dataframe to get only the matches played by the team
    team_results_df = football_results_df[
        (football_results_df['home_team']==team_name)  | 
        (football_results_df['away_team']==team_name)
        ]
    return team_results_df

def stats_of_team(team_results_df, team_name):
    """
    This function takes a dataframe as input and returns the number of matches played, won, lost, and drawn by the team(s).
    """
    # number of matches played by the team
    number_of_matches = len(team_results_df)

    # number of games won by the team
    wins = len(team_results_df[
        (team_results_df['home_team']==team_name) & 
        (team_results_df['home_score'] > team_results_df['away_score'])
        ]) + len(team_results_df[
        (team_results_df['away_team']==team_name) & 
        (team_results_df['away_score'] > team_results_df['home_score'])
        ])
    
        # number of games lost by the team
    losses = len(team_results_df[
        (team_results_df['home_team']==team_name) & 
        (team_results_df['home_score'] < team_results_df['away_score'])
        ]) + len(team_results_df[
        (team_results_df['away_team']==team_name) & 
        (team_results_df['away_score'] < team_results_df['home_score'])
        ])
    
    # number of games drawn by the team
    draws = len(team_results_df[
        (team_results_df[('home_team')]==team_name) & 
        (team_results_df[('home_score')] == team_results_df[('away_score')])
        ]) + len(team_results_df[
        (team_results_df[('away_team')]==team_name) & 
        (team_results_df[('away_score')] == team_results_df[('home_score')])
        ])
    
    return number_of_matches, wins, losses, draws






# Example usage
# the number of matches played by the Republic of Ireland
team_results_df  = isolate_team('Italy')
print(team_results_df.head())

"""
ire_football_results_df = football_results_df[
    (football_results_df[('home_team')]=='Republic of Ireland')  | 
    (football_results_df[('away_team')]=='Republic of Ireland')
    ]
print(ire_football_results_df.head())

print('The number of matches played by the Republic of Ireland is:', len(ire_football_results_df))

# the number of matches Ireland have won 
ire_wins = len(ire_football_results_df[
    (ire_football_results_df[('home_team')]=='Republic of Ireland') & 
    (ire_football_results_df[('home_score')] > ire_football_results_df[('away_score')])
    ]) + len(ire_football_results_df[
    (ire_football_results_df[('away_team')]=='Republic of Ireland') & 
    (ire_football_results_df[('away_score')] > ire_football_results_df[('home_score')])
    ])
print('The number of matches won by the Republic of Ireland is:', ire_wins)
"""