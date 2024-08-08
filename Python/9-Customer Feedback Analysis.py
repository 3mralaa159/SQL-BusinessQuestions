# Question
  Capital One's' marketing team is working on a project to analyze customer feedback from their feedback surveys.
  The team sorted the words from the feedback into three different categories;
  •	short_comments
  •	mid_length_comments
  •	long_comments
  The team wants to find comments that are not short and that come from social media.
  The output should include 'feedback_id,' 'feedback_text,' 'source_channel,' and a calculated category.

# Link
  https://platform.stratascratch.com/coding/10366-customer-feedback-analysis?code_type=1

# Answer 
# Import your libraries
import pandas as pd

# Start writing code
customer_feedback.head()
df = customer_feedback.copy()
# Filter to social media only
df = df[df['source_channel']=='social_media']
# Create a function to sort the words from the feedback into three different categories
def cal(x):
    if len(x) < 40:
        return 'short'
    elif 41 < len(x) < 80:
        return 'mid'
    else:
        return 'long'
# Apply the func and filter 
df['calculated_category'] = df['feedback_text'].apply(cal)
df.query("calculated_category != 'short'")
