# Question
  Meta/Facebook sends SMS texts when users attempt to 2FA (2-factor authenticate) into the platform to log in.
  In order to successfully 2FA they must confirm they received the SMS text message. Confirmation texts are only valid on the date they were sent.
Unfortunately, there was an ETL problem with the database where friend requests and invalid confirmation records were inserted into the logs,
  which are stored in the 'fb_sms_sends' table. These message types should not be in the table.
Fortunately, the fb_confirmers table contains valid confirmation records so you can use this table to identify SMS text messages that were confirmed by the user.



# Link
  https://platform.stratascratch.com/coding/10291-sms-confirmations-from-users?code_type=2

# Answer
# Step 1: Filter the fb_sms_sends DataFrame
filtered_sms_sends = fb_sms_sends[
    (fb_sms_sends['ds'] == '2020-08-04') & 
    (fb_sms_sends['type'] == 'message')
]

# Step 2: Merge with fb_confirmers DataFrame
merged_data = pd.merge(
    filtered_sms_sends, 
    fb_confirmers, 
    left_on=['phone_number', 'ds'], 
    right_on=['phone_number', 'date'], 
    how='left'
)

# Step 3: Calculate the percentage of confirmed SMS texts
total_messages = len(filtered_sms_sends)
confirmed_messages = merged_data['date'].notna().sum()
confirmed_percentage = (confirmed_messages / total_messages) * 100

print(f"Confirmed SMS percentage for August 4, 2020: {confirmed_percentage:.2f}%")
