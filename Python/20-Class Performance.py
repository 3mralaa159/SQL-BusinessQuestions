# Question
  You are given a table containing assignment scores of students in a class. Write a query that identifies the largest difference in total score  of all assignments.
Output just the difference in total score (sum of all 3 assignments) between a student with the highest score and a student with the lowest score.

# Link
  https://platform.stratascratch.com/coding/10310-class-performance?code_type=1

# Answer.1
df['total_score'] = df['assignment1'] + df['assignment2'] + df['assignment3']

result = df['total_score'].max() - df['total_score'].min()


# Answer.2
import sqlite3

# database connection
conn = sqlite3.connect('your_database.db')

# Create a cursor object
cursor = conn.cursor()

# Query to get the maximum and minimum total scores
query = """
SELECT 
    MAX(total_score) - MIN(total_score) AS max_score_difference
FROM (
    SELECT 
        (assignment1 + assignment2 + assignment3) AS total_score
    FROM 
        box_scores
) AS scores;
"""

# Execute the query
cursor.execute(query)

# Fetch the result
result = cursor.fetchone()

# Extract the difference
max_score_difference = result[0]

# Print the result
print(f"The largest difference in total score is: {max_score_difference}")

# Close the connection
conn.close()
