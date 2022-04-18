import requests

url = "https://api.sheety.co/917a493d299bb9a04c196c7cf0393353/apiSciencesPo/responses"

def get_data():
    r = requests.get(url)
    return r.json()['responses']

def add_row():
  data = {
      "response": {
          "lon": "2.3580603,",
          "lat": "48.8734703",
          "comment" : "add from python script"
      }
  }
  
  response = requests.post(url=url, json=data)
  print("response.status_code =", response.status_code)
  print("response.text =", response.text)

def edit_row(id, key, text):
  id = id
  data = {
    "response": {
        key: text,
    }
  }
  endpoint = f"{url}/{id}"
  
  response = requests.put(url=endpoint, json=data) 
  print("response.status_code =", response.status_code) 
  print("response.text= ", response.text)

add_row() #add row in excel sheet
edit_row(5,'comment', 'new comment from python script !!!')

#get all rows from excel sheet
resp = get_data()

#iterate on each response
for i in resp:
    print(i['lon'], i['lat'])
    print (i['comment'])
    print('')
