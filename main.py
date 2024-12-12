import pandas as pd
import numpy as np


df = pd.read_csv('output.csv')


###### MATCH DATASET
def create_match_dataset():
    #Select columns to use
    match_df = df[['match_id','match_name','team_id','is_home','goals_scored']]


    #SPlit df in teams playing home and away ans sum goals scored en each game
    home_teams = match_df[match_df['is_home']==True].groupby(by=['match_id','match_name'], as_index=False).sum().rename(columns={'team_id':'home_team_id','goals_scored':'home_goals'})
    away_teams = match_df[match_df['is_home']==False].groupby(by=['match_id','match_name'], as_index=False).sum().rename(columns={'team_id':'away_team_id','goals_scored':'away_goals'})

    #Merge dataframe together
    match_df = pd.merge(
        home_teams[['match_id', 'match_name', 'home_team_id', 'home_goals']],
        away_teams[['match_id', 'away_team_id', 'away_goals']],
        on='match_id'
    )

    # Rearrange columns for correct order
    match_df = match_df[['match_id','match_name', 'home_team_id', 'away_team_id', 'home_goals', 'away_goals']]
    match_df.to_csv('match.csv', index=False)


###### TEAM DATASET
def create_team_dataset():
    #Select columns to use
    team_df = df[['match_id','match_name','team_id','is_home']]

    #split by teams playing home and away
    home_team_df =team_df[team_df['is_home']==True].groupby(by=['team_id','match_name'], as_index=False).agg({'match_name':'first'})
    away_team_df =team_df[team_df['is_home']==False].groupby(by=['team_id','match_name'], as_index=False).agg({'match_name':'first'})

    #For teams playing home select the first name, for away, select the second
    home_team_df['match_name'] = home_team_df['match_name'].apply(lambda x: x.split(' vs ')[0])
    away_team_df['match_name'] = away_team_df['match_name'].apply(lambda x: x.split(' vs ')[1])

    #Concat df and drop duplicates
    team_df = pd.concat([home_team_df, away_team_df])
    team_df = team_df.drop_duplicates()

    team_df.to_csv('team.csv', index=False)

###### PLAYER DATASET
def create_player_dataset():
    #Select columns to use
    player_df = df[['player_id','team_id','player_name']]

    #Drop duplicates and order by team for easier reading
    player_df = player_df.drop_duplicates().sort_values(by='team_id')

    player_df.to_csv('player.csv', index=False)



###### STATISTICS DATASET
def create_statistics_dataset():
    #Select columns to use
    stat_df = df[['player_id', 'match_id', 'goals_scored', 'minutes_played']]

    #Aux df to alculate goals soed en each game
    aux_df = df[['match_id','goals_scored']]


    #Group by player performance in each game and add new index
    stat_df.groupby(by=['player_id','match_id']).agg({'goals_scored':'first','minutes_played':'first'}).reset_index()

    #Find percentage of minuted played and round value
    stat_df['fraction_of_total_minutes_played'] = round(stat_df['minutes_played'] / 90,2)

    #Calculate goals scored in each game
    aux_df = df[['match_id','goals_scored']]
    aux_df = aux_df.groupby('match_id')['goals_scored'].sum().reset_index()
    aux_df.rename(columns={'goals_scored': 'total_goals_in_match'}, inplace=True)

    #Merge stat_df with ayx_df, and calculate percentage of goals scored in each game for each player
    stat_df = pd.merge(stat_df, aux_df, on='match_id')
    stat_df['fraction_of_total_goals_scored'] = round(stat_df['goals_scored'] / stat_df['total_goals_in_match'],2)


    # Rearrange columns for correct order
    stat_df = stat_df[['player_id','match_id','goals_scored','minutes_played','fraction_of_total_minutes_played','fraction_of_total_goals_scored']]
    stat_df.index.name = 'Stat_Id'

    stat_df.to_csv('statistics.csv')



if __name__ == '__main__':
    print("Creating match dataset")
    create_match_dataset()

    print("Creating team dataset")
    create_team_dataset()

    print("Creating player dataset")
    create_player_dataset()

    print("Creating statistic dataset")
    create_statistics_dataset()