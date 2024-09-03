# Question
  Meta/Facebook sends SMS texts when users attempt to 2FA (2-factor authenticate) into the platform to log in.
  In order to successfully 2FA they must confirm they received the SMS text message. Confirmation texts are only valid on the date they were sent.
Unfortunately, there was an ETL problem with the database where friend requests and invalid confirmation records were inserted into the logs,
  which are stored in the 'fb_sms_sends' table. These message types should not be in the table.
Fortunately, the 'fb_confirmers' table contains valid confirmation records so you can use this table to identify SMS text messages that were confirmed by the user.

# Link
  https://platform.stratascratch.com/coding/10291-sms-confirmations-from-users?code_type=2

# Answer
WITH valid_messages AS (
    SELECT
        sms.ds,
        sms.phone_number
    FROM
        fb_sms_sends sms
    WHERE
        sms.ds = '2020-08-04'
        AND sms.type = 'message'
)
SELECT
    COUNT(c.phone_number) * 100.0 / COUNT(vm.phone_number) AS confirmed_percentage
FROM
    valid_messages vm
LEFT JOIN
    fb_confirmers c
ON
    vm.phone_number = c.phone_number
    AND vm.ds = c.date
WHERE
    c.phone_number IS NOT NULL;
  


