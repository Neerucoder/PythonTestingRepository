import requests
import json
import jsonpath

URLTested = "https://gorest.co.in/public-api/users/123"

def test_update_user():
  file = open('C:/Users/neera/Downloads/TestCases/example.json','r')
  file_json = file.read()
  request_json = json.loads(file_json)
  response4 = requests.put(URLTested,request_json)

  responsedoublecheck = json.loads(response4.text)
  newData = jsonpath.jsonpath(responsedoublecheck,'code')
  print(newData)
