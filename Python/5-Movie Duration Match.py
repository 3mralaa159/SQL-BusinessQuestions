# Question
  '(As a data scientist at Amazon Prime Video, you are tasked with enhancing the in-flight entertainment experience for Amazon’s airline partners.
  Your challenge is to develop a feature that suggests individual movies from Amazon's content database that fit within a given flight's duration.
  For flight 101, find movies whose runtime is less than or equal to the flight's duration.)'

# Link
  https://platform.stratascratch.com/coding/10360-movie-duration-match?code_type=2
# Answer 
# Import your libraries
import pandas as pd
# code
entertainment_catalog.head()
# Perform a cross join (Cartesian product) between DataFrames
df = pd.merge(entertainment_catalog,flight_schedule,how='cross')
# Filter rows where movie duration is less than or equal to flight duration
re = df.query('duration <= flight_duration')
# Select flight_id, movie_id, and duration columns, and sort by flight_id
ree = re.loc[:,['flight_id','movie_id','duration']].sort_values('flight_id')
# Filter for flight_id == 101
ree[ree['flight_id'] == 101]
