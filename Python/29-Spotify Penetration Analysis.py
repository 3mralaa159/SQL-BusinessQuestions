# Question
  Market penetration is an important metric for understanding Spotifys performance and growth potential in different regions.
You are part of the analytics team at Spotify and are tasked with calculating the active user penetration rate in specific countries.
For this task, active_users' are defined based on the  following criterias:
last_active_date: The user must have interacted with Spotify within the last 30 days.
•    sessions: The user must have engaged with Spotify for at least 5 sessions.
•    listening_hours: The user must have spent at least 10 hours listening on Spotify.
Based on the condition above, calculate the active 'user_penetration_rate' by using the following formula.
•    Active User Penetration Rate = (Number of Active Spotify Users in the Country / Total users in the Country)
Total Population of the country is based on both active and non-active users.
The output should contain 'country' and active_user_penetration_rate rounded to 2 decimals.
Lets assume the current_day is 2024-01-31.

# Link  
  https://platform.stratascratch.com/coding/10369-spotify-penetration-analysis?code_type=1

# Answer
df = penetration_analysis.copy()
total = df.groupby('country')['user_id'].count().reset_index()
active = df[(df['last_active_date'] >= ' 2024-01-01') & (df['listening_hours'] >10) &(df['sessions'] >= 5)]

active = active.groupby('country')['user_id'].count().reset_index()
merged=pd.merge(total,active,on='country')
merged['penetration']=merged['user_id_y']*100/merged['user_id_x']
merged['penetration'] = np.round(merged['penetration'],2)
merged[['country','penetration']]
