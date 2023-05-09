import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
def apiApp():
	account_sid = "AC3eac6945f78f6d01c69ca0f6e57d9317"
	auth_token = "760dffb099028531973ac9252f2d09aa"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
	  body="Accident is Detected",
	  from_="+13203628692",
	  to="+919431893084"
	)
	print(message.sid)
