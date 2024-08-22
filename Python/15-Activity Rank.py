# Question
  Find the email activity rank for each user. Email activity rank is defined by the total number of emails sent.
  The user with the highest number of emails sent will have a rank of 1, and so on. Output the user, total emails, and their activity rank. Order records by the total emails in descending order.
  Sort users with the same number of emails in alphabetical order.
In your rankings, return a unique value (i.e., a unique rank) even if multiple users have the same number of emails. For tie breaker use alphabetical order of the user usernames.

# Link
  https://platform.stratascratch.com/coding/10351-activity-rank?code_type=1


# Answer
df = df.groupby('from_user')['to_user'].count().reset_index()
df['rank']=df['to_user'].rank(method = 'dense',ascending=False)
df = df.sort_values('rank',ascending=True)


# Answer.2
result = google_gmail_emails.groupby(
    ['from_user']).size().to_frame('total_emails').reset_index()
result['rank'] = result['total_emails'].rank(method='first', ascending=False)
result = result.sort_values(by=['total_emails', 'from_user'], ascending=[False, True])
