# Question
  What is the overall friend acceptance rate by date?
  Your output should have the rate of acceptances by the date the request was sent. Order by the earliest date to latest.
Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver)
that s logged in the table with action = 'sent'. If the request is accepted, the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.

# Link
  https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?code_type=1

# Answer
# Count sent requests
sent_requests = fb_friend_requests[fb_friend_requests['action'] == 'sent'] \
    .groupby(fb_friend_requests['date'].dt.date).size().reset_index(name='total_sent')

# Count accepted requests
accepted_requests = fb_friend_requests[fb_friend_requests['action'] == 'accepted'] \
    .groupby(fb_friend_requests['date'].dt.date).size().reset_index(name='total_accepted')

# Merge the sent and accepted counts on the date
merged = pd.merge(sent_requests, accepted_requests, how='left', left_on='date', right_on='date')

# Fill NaN values in total_accepted with 0
merged['total_accepted'].fillna(0, inplace=True)

# Calculate the acceptance rate
merged['acceptance_rate'] = merged['total_accepted'] / merged['total_sent']

# Display the result ordered by date
result = merged.sort_values('date')
print(result)
