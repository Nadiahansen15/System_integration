import requests
from get_name import name
from get_last_name import last_name
from get_email import email
from get_phone import phone
from api_key import apikey

message = f"hi {name} {last_name}, you email is {email}"
print (phone)
print (message)

url = "https://fatsms.com/send-sms"
data = {"to_phone": phone, "message": message, "api_key": apikey}

print (requests.post(url, data).text)

