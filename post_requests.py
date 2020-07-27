import requests
import json
import jsonpath
url = "https://reqres.in/api/users/"

# post is used for creating; put is used for updating

# read json file
json_file = open("/Users/ajayvidekar/Desktop/RESUME/create_user.json", "r")
json_input = json_file.read()

requests_json = json.loads(json_input)
#print(requests_json)

# make post request using json and request module
response = requests.post(url, requests_json)
print(response.content)
#print(response.status_code)

# validate response code
assert  response.status_code == 201

# fetch header info from response
print(response.headers)

print(response.headers.get('Content-Length'))

# parse response from json format. (currently in string format)
response_json = json.loads(response.text)

# pick ID using json path, (from the data returned)
id = jsonpath.jsonpath(response_json, 'id') # will always return list
print(id[0])

