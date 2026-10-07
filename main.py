import requests
from twilio.rest import Client
import os
account_sid = "ACce6e16e6d9daf6036a605a4ac3972b0d"
auth_token = "0c2c0663946070ab4f1c7566292cffd7"

prameter = {
    "lat": "22.5726",
    "lon": "88.3639",
    "appid": "dcef4448ee8629e5bc4a52cda21c494f",
    "cnt": 4
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast',prameter)
response.raise_for_status()
print(response.json())
json_data = response.json()
for item in json_data['list']:
    if item['weather'][0]["id"] < 700:
        print("Its rainign please bring umbrella")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= "sms_event_notifications",
            from_="+17372508034",
            to="+918145981844"
        )
        print(message.status)
    else:
        print("Its sunny weather")

