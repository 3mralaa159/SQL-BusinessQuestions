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
-------------------------------------------------------------------
# Answer.2
# Import your libraries
import pandas as pd

# Start writing code
customer_feedback.head()
df = customer_feedback.copy()
# Filter to social media only
df = df[df['source_channel']=='social_media']
bins =[0,40,80,200]
labels =['short','mid','long']
data = df['feedback_text'].apply(lambda x : len(x))
df['calculated category'] = pd.cut(data,bins,labels=labels)
df[(df['source_channel']=='social_media')&(df['calculated category']!='short')]
-------------------------------------------------------------------
# Answer.3
import pandas as pd

# Assuming customer_feedback is already defined
df = customer_feedback.copy()

# Filter to social media only
df = df[df['source_channel'] == 'social_media']

# Define the mapping function
def categorize_text_length(length):
    if length <= 40:
        return 'short'
    elif 40 < length <= 80:
        return 'mid'
    else:
        return 'long'

# Apply the function using map
df['calculated_category'] = df['feedback_text'].apply(len).map(categorize_text_length)

# Filter out 'short' feedbacks
result_df = df[df['calculated_category'] != 'short']

# Display the resulting DataFrame
result_df.head()
