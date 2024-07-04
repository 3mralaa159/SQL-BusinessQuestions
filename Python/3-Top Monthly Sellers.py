# Question
  You are provided with a transactional dataset from Amazon that contains detailed information about sales across different products and marketplaces.
  Your task is to list the top 3 sellers in each product category for January.
  The output should contain 'seller_id' , 'total_sales' ,'product_category' , 'market_place', and 'month'.
# Link
  https://platform.stratascratch.com/coding/10362-top-monthly-sellers?code_type=2
# Answer
# Import your libraries
import pandas as pd

# code
sales_data.head()

# Filter transactions for January
january_df = sales_data[sales_data['month'].dt.month == 1]

# Group by product_category and seller_id, summing total_sales
category_seller_sales = january_df.groupby(['product_category', 'seller_id']).agg(total_sales=('total_sales', 'sum')).reset_index()

# Sort within each category by total_sales descending and get top 3 sellers
top_sellers = category_seller_sales.groupby('product_category').apply(lambda x: x.nlargest(3, 'total_sales')).reset_index(drop=True)

# Add columns 
top_sellers['market_place'] = sales_data['market_place']
top_sellers['month'] = 'Jan'
# Display the results
print(top_sellers[['seller_id', 'total_sales', 'product_category','market_place','month']])

