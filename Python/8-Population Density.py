# Question
  You are working on a data analysis project at Deloitte where you need to analyze a dataset containing information
about various cities. Your task is to calculate the population density of these cities, rounded to the nearest integer, and identify the cities with the minimum and maximum densities.
The population density should be calculated as (Population / Area).
The output should contain 'city', 'country', 'density'.

# Link
  https://platform.stratascratch.com/coding/10368-population-density?code_type=2

# Answer 
# Import your libraries
import pandas as pd

# Start writing code
cities_population.head()
df = cities_population.copy().reset_index()
# Filter 
df = df.query('area != 0')
df['density'] = round(df['population'] / df['area'])
df
# Find index position of max and min values of density 
nn = df['density'].idxmin()
n = df['density'].idxmax()
# fect data from DataFrame
df.loc[[n,nn],[ 'city', 'country', 'density']]

# Answer.2
import pandas as pd 
df = pd.DataFrame(cities_population)
df['density'] = df.apply(lambda row: (row['population'] / row['area']) if row['area'] > 0 else None, axis=1)
df = df.dropna(subset=['density'])  # Drop rows where density calculation was not possible
df['density'] = df['density'].round().astype(int)

# Identify city with minimum density
min_density_city = df.nsmallest(1, 'density')

# Identify city with maximum density
max_density_city = df.nlargest(1, 'density')

# Output results
result = pd.concat([min_density_city, max_density_city])
print(result[['city', 'country', 'density']])
