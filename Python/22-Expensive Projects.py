# Question
  Given a list of projects and employees mapped to each project, calculate by the amount of project budget allocated to each employee .
The output should include the project title and the project budget rounded to the closest integer. Order your list by projects with the highest budget per employee first.

# Link
  https://platform.stratascratch.com/coding/10301-expensive-projects?code_type=1

# Answer
 Merge the two DataFrames on project ID
merged_df = pd.merge(ms_projects, ms_emp_projects, left_on='id', right_on='project_id')

# Group by project ID and calculate the budget per employee
grouped = merged_df.groupby(['id', 'title', 'budget']).size().reset_index(name='employee_count')
grouped['budget_per_employee'] = np.round(grouped['budget'] / grouped['employee_count'])

# Sort by the highest budget per employee
result = grouped.sort_values(by='budget_per_employee', ascending=False)

# Select and rename columns for the final output
result = result[['title', 'budget', 'budget_per_employee']]
