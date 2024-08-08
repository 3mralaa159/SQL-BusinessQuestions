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
select * ,
case 
when LENGTH(feedback_text) < 25 then 'short'
when LENGTH(feedback_text) between 26 and 75 then 'mid'
else 'long'
end as calculated_category
from customer_feedback 
where source_channel ='social_media' 
and LENGTH(feedback_text) > 25;
