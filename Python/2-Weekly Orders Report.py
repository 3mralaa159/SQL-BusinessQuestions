# Question
  For each week, find the total number of orders. Include only the orders that are from the first quarter of 2023.
# link
  https://platform.stratascratch.com/coding/10363-weekly-orders-report?code_type=2

# Answer
# Import your libraries
import pandas as pd
# code
orders_analysis.head()
# sum by week 
total = orders_analysis.groupby('week')['quantity'].sum()
# create new dataframe with each week and sum of quantity
df = pd.DataFrame({'week':total.index ,
'quantity':total.values
})
# change into date format to filter 
df['week'] = pd.to_datetime(df['week'])
df['week'] = df['week'].dt.strftime('%Y-%m-%d')
df[df['week'] < '2023-04-01']
