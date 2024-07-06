# Question
  Find doctors with the last name of 'Johnson' in the employee list. The output should contain both their first and last names.
# Link
  https://platform.stratascratch.com/coding/10356-finding-doctors?code_type=1
# Answer
# Import your libraries
import pandas as pd
# code
employee_list.head()

df = employee_list[['first_name','last_name']]
df[df['last_name'] == 'Johnson'].sort_values('first_name')
