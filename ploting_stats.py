# in this program we will plot the stats of the football teams

import matplotlib.pyplot as plt
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
    categories = ['Wins', 'Losses', 'Draws']
    values = [wins, losses, draws]
    
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'green', 'red', 'orange'])
    plt.title(f'Stats for Team(s): {", ".join(team_names)} , Matches Played: {number_of_matches}')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.ylim(0, max(values) + 1)
    
    # Save the plot to a file instead of showing it (for headless environments)
    plt.savefig(f"{team_names}_team_stats_bar_chart.png")
    print(f"Plot saved as {team_names}_team_stats_bar_chart.png")

    # create pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'red', 'orange'])
    plt.title(f'Stats for Team(s): {", ".join(team_names)}')
    # Save the pie chart to a file
    plt.savefig(f"{team_names}_team_stats_pie_chart.png")
    print(f"Pie chart saved as {team_names}_team_stats_pie_chart.png")


# Example usage
if __name__ == "__main__":
    # Define the team names to plot
    team_names_example = ['Italy', 'Spain', 'Germany']
    
    # Plot the stats for the specified teams
    plot_team_stats(team_names_example)