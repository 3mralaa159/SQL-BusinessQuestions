# Question
  Find the email activity rank for each user. Email activity rank is defined by the total number of emails sent.
  The user with the highest number of emails sent will have a rank of 1, and so on. Output the user, total emails, and their activity rank. Order records by the total emails in descending order.
  Sort users with the same number of emails in alphabetical order.
In your rankings, return a unique value (i.e., a unique rank) even if multiple users have the same number of emails. For tie breaker use alphabetical order of the user usernames.

# Link
  https://platform.stratascratch.com/coding/10351-activity-rank?code_type=1


# Answer
with one as (select from_user , count(*) 
from google_gmail_emails
group by 1 
order by 2 desc , 1 asc) ,
two as (select * , dense_rank() over(order by count desc)
from one)
select *
from two 

# Answer.2
SELECT  from_user, 
        count(*) as total_emails, 
        row_number() OVER ( order by count(*) desc, from_user asc)
    FROM google_gmail_emails 
    GROUP BY from_user
    order by 2 DESC, 1
