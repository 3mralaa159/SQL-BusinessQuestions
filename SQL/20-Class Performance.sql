# Question
  You are given a table containing assignment scores of students in a class. Write a query that identifies the largest difference in total score  of all assignments.
Output just the difference in total score (sum of all 3 assignments) between a student with the highest score and a student with the lowest score.

# Link
  https://platform.stratascratch.com/coding/10310-class-performance?code_type=1

# Answer
SELECT 
    MAX(total_score) - MIN(total_score) AS max_score_difference
FROM (
    SELECT 
        (assignment1 + assignment2 + assignment3) AS total_score
    FROM 
        box_scores
) AS scores;
