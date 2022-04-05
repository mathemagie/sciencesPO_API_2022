import requests
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'XXX'
auth_token = 'XXX'
client = Client(account_sid, auth_token)


def send_sms(content_sms='test'): 
  message = client.messages.create(
    body=content_sms,
    from_='+19388887362',
    to='+330620838825')
  print(message.sid)

send_sms('bonjour API')

def get_cc(lon,lat):
  url = "https://api.geoapify.com/v1/geocode/reverse?lat={}&lon={}&format=json&apiKey=d90b1a594bb84aebab6bfac77b29ccf0".format(lat,lon)
  r = requests.get(url)
  return r.json()['results'][0]['formatted']

def get_trad(text):
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
  }
  
  data = 'auth_key=e863711d-db14-1ae6-e421-be1c08f253a5:fx&text={}&target_lang=FR'.format(text)
  
  response = requests.post('https://api-free.deepl.com/v2/translate', headers=headers, data=data)
  return response.json()

def get_data():
  url = "https://api.sheety.co/75b80a29977172c897e968cc7509c3f6/apiSciencesPo/sheet1"
  r = requests.get(url)
  return r.json()['sheet1']

resp = get_data()
for i in resp:
  print(i['lon'],i['lat'])
  cc = get_cc(i['lon'],i['lat'])
  print(cc)
  print(get_trad(i['comment']))
  print()
