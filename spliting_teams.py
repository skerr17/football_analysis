# in this program we will split define a function that will 
# isolate a given team into its own dataframe

# import impport_dataset to get the dataframe of football results
from import_dataset import football_results_df

# Note documentation for .isin() method https://www.geeksforgeeks.org/python-pandas-dataframe-isin/


def isolate_teams(team_names):
    """
    This function takes a list of team names as input and returns a dataframe,
    containing only the matches played by those team(s).
    """

    # covert the input if it is a string to a list
    if isinstance(team_names, str):
        team_names = [team_names]
    # filter the dataframe to get only the matches played by the team
    team_results_df = football_results_df[
        (football_results_df['home_team'].isin(team_names))  | 
        (football_results_df['away_team'].isin(team_names))
        ]
    return team_results_df

def stats_of_team(team_results_df, team_names):
    """
    This function takes a dataframe as input and returns the number of matches played, won, lost, and drawn by the team(s).
    """
    # convert the input if it is a string to a list
    if isinstance(team_names, str):
        team_names = [team_names]

    # number of matches played by the team
    number_of_matches = len(team_results_df)

    # number of games won by the team
    wins = len(team_results_df[
        ((team_results_df['home_team'].isin(team_names)) & (team_results_df['home_score'] > team_results_df['away_score'])) |
        ((team_results_df['away_team'].isin(team_names)) & (team_results_df['away_score'] > team_results_df['home_score']))
    ])

    # number of games lost by the team
    losses = len(team_results_df[
        ((team_results_df['home_team'].isin(team_names)) & (team_results_df['home_score'] < team_results_df['away_score'])) |
        ((team_results_df['away_team'].isin(team_names)) & (team_results_df['away_score'] < team_results_df['home_score']))
    ])

    # number of games drawn by the team
    draws = len(team_results_df[
        (team_results_df['home_score'] == team_results_df['away_score']) &
        ((team_results_df['home_team'].isin(team_names)) | (team_results_df['away_team'].isin(team_names)))
    ])

    return number_of_matches, wins, losses, draws






# Example usage
if __name__ == "__main__":
    # the number of matches played by the team Italy, Spain, and Germany
    team_names_example = ['Italy', 'Spain', 'Germany']
    team_results_df  = isolate_teams(team_names_example)

    # get the number of matches played, won, lost, and drawn by the team
    number_of_matches, wins, losses, draws = stats_of_team(team_results_df, team_names_example)
    print(f"Number of matches played by {team_names_example}: {number_of_matches}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Draws: {draws}")