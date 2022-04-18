import requests

def get_data():
    url = "https://api.sheety.co/917a493d299bb9a04c196c7cf0393353/apiSciencesPo/responses"
    r = requests.get(url)
    return r.json()['responses']


resp = get_data()

for i in resp:
    print(i['lon'], i['lat'])
    print('')

