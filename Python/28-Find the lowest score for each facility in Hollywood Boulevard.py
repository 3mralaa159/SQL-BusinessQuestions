# Question
  Find the lowest score per each facility in Hollywood Boulevard.
Output the result along with the corresponding facility name.
Order the result based on the lowest score in descending order and the facility name in the ascending order.

# Link
  https://platform.stratascratch.com/coding/10180-find-the-lowest-score-for-each-facility-in-hollywood-boulevard?code_type=1

# Answer
result = df_hollywood.groupby('facility_name')['score'].min().reset_index()

# Sort by lowest score in descending order and facility name in ascending order
result = result.sort_values(by=['score', 'facility_name'], ascending=[False, True])

# Rename the columns for clarity
result.columns = ['facility_name', 'lowest_score']
