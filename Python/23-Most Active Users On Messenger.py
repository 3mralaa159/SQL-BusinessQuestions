# Question
  Meta/Facebook Messenger stores the number of messages between users in a table named 'fb_messages'.
In this table 'user1' is the sender, 'user2' is the receiver, and 'msg_count' is the number of messages exchanged between them.
Find the top 10 most active users on Meta/Facebook Messenger by counting their total number of messages sent and received. 
Your solution should output usernames and the count of the total messages they sent or received

# Link
  https://platform.stratascratch.com/coding/10295-most-active-users-on-messenger?code_type=1

# Answer
# Calculate total messages sent by each user (user1)
sent_messages = fb_messages.groupby('user1')['msg_count'].sum().reset_index()
sent_messages.columns = ['user_name', 'total_messages']

# Calculate total messages received by each user (user2)
received_messages = fb_messages.groupby('user2')['msg_count'].sum().reset_index()
received_messages.columns = ['user_name', 'total_messages']

# Combine sent and received messages
combined = pd.concat([sent_messages, received_messages])

# Aggregate to find the total messages for each user
total_messages = combined.groupby('user_name')['total_messages'].sum().reset_index()

# Sort by the total message count in descending order and get the top 10 users
top_users = total_messages.sort_values(by='total_messages', ascending=False).head(10)
