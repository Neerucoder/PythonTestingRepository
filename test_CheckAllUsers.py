import requests
import json
import jsonpath

def test_get_all_users():#Building GET Request Test Cases
  URLTested = "https://gorest.co.in/public-api/users"
  response = requests.get(URLTested)
  print("Response: ",response) #Checking Response
  print("Content: ",response.content) #Checking Content
  print(response.text) #Printing Text data of Request
  assert response.status_code == 200
  requests.get(URLTested, verify=True)
  print("Header: ",response.headers) #Loading Headers
  json_response = json.loads(response.text) #Getting Response in JSON Format
  print("JSON: ", json_response)
  pages = jsonpath.jsonpath(json_response,'data') #Getting Total Pages
  print(pages)
  payload = { 'gender': 'Female'}
  payload2 = { 'gender': 'Male'}
  r = requests.get(URLTested, params=payload)
  r2 = requests.get(URLTested, params=payload2)
  print("Request with Male Payload: ", r2)
  print("Request with Female Payload: ",r)
  print("Female Payload Request content: ",r.content)
  print("Male Payload Request content: ",r2.content)