# Question
  Identify projects that are at risk for going overbudget. A project is considered to be overbudget 
if the cost of all employees assigned to the project is greater than the budget of the project.
You wil need to prorate the cost of the employees to the duration of the project. 
For example,
if the budget for a project that takes half a year to complete is $10K, then the total half-year salary of all employees assigned to the project should not exceed $10K.
Salary is defined on a yearly basis, so be careful how to calculate salaries for the projects that last less or more than one year.
Output a list of projects that are overbudget with their project name, project budget, and prorated total employee expense (rounded to the next dollar amount).

# Link
  https://platform.stratascratch.com/coding/10304-risky-projects?code_type=1

# Answer.1
# Merge the dataframes
merged_df = linkedin_projects.merge(linkedin_emp_projects, left_on='id', right_on='project_id') \
                             .merge(linkedin_employees, left_on='emp_id', right_on='id')

# Calculate the project duration in days
merged_df['project_duration_days'] = (merged_df['end_date'] - merged_df['start_date']).dt.days

# Prorate the employee expenses for the duration of the project
merged_df['prorated_expense'] = merged_df['project_duration_days'] * (merged_df['salary'] / 365)

# Group by project to sum up the prorated expenses
project_expenses = merged_df.groupby(['project_id', 'title', 'budget'], as_index=False) \
                            .agg({'prorated_expense': 'sum'})

# Determine projects that are overbudget
overbudget_projects = project_expenses[project_expenses['prorated_expense'] > project_expenses['budget']]

# Round up the prorated expenses to the next dollar
overbudget_projects['prorated_expense'] = np.ceil(overbudget_projects['prorated_expense'])

# Select relevant columns
overbudget_projects = overbudget_projects[['title', 'budget', 'prorated_expense']]
