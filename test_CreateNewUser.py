import requests
import json
import jsonpath

def test_create_new_user():
  file = open('C:/Users/neera/Downloads/TestCases/example1.json','r')
  file_json = file.read()
  request_json = json.loads(file_json)
  response4 = requests.post("https://gorest.co.in/public-api/users",request_json)

  responsedoublecheck = json.loads(response4.text)
  newData = jsonpath.jsonpath(responsedoublecheck,'code')
  print(newData)