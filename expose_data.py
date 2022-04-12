import requests

def get_data():
  url = "https://api.sheety.co/75b80a29977172c897e968cc7509c3f6/apiSciencesPo/sheet1"
  r = requests.get(url)
  return r.json()['sheet1']

resp = get_data()
for i in resp:
  print(i['lon'],i['lat'])
  print('')
