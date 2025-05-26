# in this program we will plot the stats of the football teams

import matplotlib.pyplot as plt
import pandas as pd
from import_dataset import football_results_df
from spliting_teams import isolate_teams, stats_of_team

# Function to plot the stats of a team
def plot_team_stats(team_names):
    """
    This function takes a list of team names as input and plots the number of matches played, won, lost, and drawn by the team(s).
    """
    # Isolate the team results
    team_results_df = isolate_teams(team_names)
    
    # Get the stats of the team
    stats = stats_of_team(team_results_df, team_names)
    

    # Unpack the stats tuple
    number_of_matches, wins, losses, draws = stats
    # Prepare data for plotting
    categories = ['Matches Played', 'Wins', 'Losses', 'Draws']
    values = [number_of_matches, wins, losses, draws]
    
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'green', 'red', 'orange'])
    plt.title(f'Stats for Team(s): {", ".join(team_names)}')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.ylim(0, max(values) + 1)
    
    # Save the plot to a file instead of showing it (for headless environments)
    plt.savefig("team_stats.png")
    print("Plot saved as team_stats.png")


# Example usage
if __name__ == "__main__":
    # Define the team names to plot
    team_names_example = ['Italy', 'Spain', 'Germany']
    
    # Plot the stats for the specified teams
    plot_team_stats(team_names_example)