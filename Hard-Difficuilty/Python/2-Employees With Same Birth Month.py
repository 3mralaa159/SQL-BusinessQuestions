# Question
Identify the number of employees within each department that share the same birth month.
  Your output should list the department, birth month, and the number of employees from that department who were born in that month.
  If a month has no employees born in it within a specific department, report this month as having 0 employees. The "profession" column stores the department names of each employee.

# Link
https://platform.stratascratch.com/coding/10355-employees-with-same-birth-month?code_type=1

# Answer.1
# Import your libraries
import pandas as pd
import numpy as np 
# Start writing code
df = employee_list.copy()

c = df.groupby(['profession','birth_month'])['employee_id'].size().reset_index(name='employee_count')
all_months = pd.Series(np.arange(1, 13),name='birth_month')
all_departments = pd.Series(df['profession'].unique(),name='profession')

merged = pd.merge(all_departments,all_months,'cross')

result = pd.merge(c,merged,on=['profession',"birth_month"],how='right').fillna(0).sort_values(by=['profession', 'birth_month'])
