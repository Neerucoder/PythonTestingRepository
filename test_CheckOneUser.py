import requests
import json
import jsonpath

URLTested = "https://gorest.co.in/public-api/users/121"

def test_get_all_data_of_one_user():#Building GET Request Test Cases for a single user data
  response = requests.get(URLTested)
  print("Response For:", URLTested)
  print("Response: ",response) #Checking Response
  print("Content: ",response.content) #Checking Content
  print(response.text) #Printing Text data of Request
  assert response.status_code == 200
  requests.get(URLTested, verify=True)
  people_json  = response.json()
  if(people_json['code']==200): #As Long as Response has data code will be 200 else it will be 404 even though status code is 200
    print(people_json['data']['id'])
    print(people_json['data']['name'])
    print(people_json['data']['email'])
    print(people_json['data']['gender'])
    print(people_json['data']['status'])
    print(people_json['data']['created_at'])
    print(people_json['data']['updated_at'])
    print("Is the User Male: ", people_json['data']['gender']=='Male') #Testing If Gender given is Male
  else:
    print(people_json['data']['message'])