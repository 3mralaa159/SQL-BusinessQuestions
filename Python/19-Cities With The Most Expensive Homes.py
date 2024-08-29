# Question
  Write a query that identifies cities with higher than average home prices when compared to the national average. Output the city names.

# Link  
  https://platform.stratascratch.com/coding/10315-cities-with-the-most-expensive-homes?code_type=1

# Answer
df = zillow_transactions.copy()

df1 = df.groupby(['state','city'])['mkt_price'].mean().reset_index()
df1['average'] = df['mkt_price'].mean()
df1[df1['mkt_price'] > df1['average']]
