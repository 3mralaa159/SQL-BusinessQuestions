# Question
  Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments.
  Output just the absolute difference in salaries.
# Link
  https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=2

# Answer
# Import your libraries
import pandas as pd
# Explore
db_employee.head()
db_dept.head()
# Merge Datsets
df = db_employee.merge(db_dept,left_on='department_id' ,right_on='id')
# filter into subsets groups
df_eng = df.query('department == "engineering"')['salary'].nlargest(1).reset_index()
df_mar = df.query('department == "marketing"')['salary'].nlargest(1).reset_index()
# Calculate difference
diff = abs(df_eng['salary'] - df_mar['salary'])
