from twillio.rest import Client

account_sid = 'ACdea1c381c3396094995d725d0c50199e'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:'
)

print(message.sid)