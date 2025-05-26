# in this program the whole projecy will be run by a user prompt for team names
# Author: Stephen Kerr

import matplotlib.pyplot as plt
from import_dataset import football_results_df
from spliting_teams import isolate_teams, stats_of_team
from ploting_stats import plot_team_stats

import os
import sys
import kagglehub
import pandas as pd

# prompt the user for team names
def get_team_names():
    """
    Prompt the user to enter team names separated by commas.
    Returns a list of team names.
    """
    valid_teams = set(football_results_df['home_team'].unique()).union(set(football_results_df['away_team'].unique()))
    while True:
        # prompt the user for team names
        team_input = input("Enter team names separated by commas: ")
        team_names = [team.strip() for team in team_input.split(',')]
        # Check if all entered names are valid
        if all(team in valid_teams for team in team_names):
            return team_names
        else:
            print("Invalid team names. Please enter valid team names from the dataset.")
    return team_names

def main():
    """
    Main function to run the program.
    It prompts the user for team names and plots their stats.
    """
    # Get team names from user input
    team_names = get_team_names()
    
    # Isolate the team results
    team_results_df = isolate_teams(team_names)
    
    # Get the stats of the team
    stats = stats_of_team(team_results_df, team_names)
    
    # Unpack the stats tuple
    number_of_matches, wins, losses, draws = stats
    
    # Prepare data for plotting
    categories = ['Matches Played', 'Wins', 'Losses', 'Draws']
    values = [number_of_matches, wins, losses, draws]

    # plot the stats of the team
    plot_team_stats(team_names)

if __name__ == "__main__":
    main()