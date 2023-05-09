import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
def apiApp():
	account_sid = "**************************"
	auth_token = "***************************"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
	  body="Accident is Detected",
	  from_="**********",
	  to="**********"
	)
	print(message.sid)
