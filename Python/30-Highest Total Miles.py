# Question
  You’re given a table of Uber rides that contains the mileage and the purpose for the business expense.
  You’re asked to find business purposes that generate the most miles driven for passengers that use Uber for their business transportation. Find the top 3 business purpose categories by total mileage.

# link
  https://platform.stratascratch.com/coding/10169-highest-total-miles?code_type=1

# Answer
 df = my_uber_drives.copy()

df = df[df['purpose'].str.len() > 0 ]

result = df.groupby('purpose')['miles'].sum().nlargest(3).reset_index()                                                                              
