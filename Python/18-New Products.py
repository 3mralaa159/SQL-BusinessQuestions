# Question
  You are given a table of product launches by company by year.
  Write a query to count the net difference between the number of products companies launched in 2020 with the number of products companies launched in the previous year.
  Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.

# Link
  https://platform.stratascratch.com/coding/10318-new-products?code_type=1


# Answer
df = df.groupby(['company_name','year'])['product_name'].size().reset_index(name='2020')
df['2019'] = df.groupby('company_name')['2020'].shift(1).fillna(0)
df = df[df['2019'] != 0]
df['diff'] =  df['2020'] - df['2019']
df[['company_name','diff']]                                                                         

                                                                        
