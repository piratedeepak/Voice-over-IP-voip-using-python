from twilio.rest import TwilioRestClient


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'PASTE ACCOUNT NUMBER HERE'
auth_token = 'PASTE TOKEN HERE'
client = TwilioRestClient(account_sid, auth_token)

message = client.messages \
                .create(
                     body="TYPE YOUR MESSAGE",
                     from_='nUMBER PROVIDE BY TWILIO',
                     to='TO WHOM YOU WANNA TO SEND'
                 )

print(message.sid)