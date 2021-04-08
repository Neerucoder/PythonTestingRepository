import requests
import json
import jsonpath

URLDelete = "https://gorest.co.in/public-api/users/123"

def test_delete_user():
  response3 = requests.delete(URLDelete)
  people_json  = response3.json()
  print(people_json['code']==404)
  assert people_json['code']==404