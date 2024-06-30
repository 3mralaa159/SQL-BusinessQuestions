# Question
    You're tasked with analyzing a Spotify-like dataset that captures user listening habits.
    For each user, calculate the total listening time and the count of unique songs they've listened to. 
    In the database duration values are displayed in seconds. Round the total listening duration to the nearest whole minute.
# link
    https://platform.stratascratch.com/coding/10367-aggregate-listening-data?code_type=1
# Answwer:
Import your libraries
import pandas as pd

# Start writing code
listening_habits.head()
# Convert duration from seconds to minutes 
listening_habits['listen_duration_minutes'] = listening_habits['listen_duration']//60
# Calculate total listening time (rounded to nearest whole minute)
total_listening_time = listening_habits.groupby('user_id')['listen_duration_minutes'].sum().round()
# Calculate count of unique songs
unique_song_count = listening_habits.groupby('user_id')['song_id'].nunique()

# Combine results into a DataFrame
result_df = pd.DataFrame({
    'user_id': total_listening_time.index,
    'total_listening_time_minutes': total_listening_time.values,
    'unique_songs_count': unique_song_count.values
})
