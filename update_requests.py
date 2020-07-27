# update requests are always 200
# post is always 201

import requests
import json
import jsonpath
url = "https://reqres.in/api/users/2"

# post is used for creating; put is used for updating

# read json file
json_file = open("/Users/ajayvidekar/Desktop/RESUME/create_user.json", "r")
json_input = json_file.read()

# parse data into json format
requests_json = json.loads(json_input)
#print(requests_json)

# make put request using json and request module
response = requests.put(url, requests_json)
print(response.content)
#print(response.status_code)

# validate response code
assert  response.status_code == 200

# parse response content
response_json = json.loads(response.text)
timestamp = jsonpath.jsonpath(response_json, "updatedAt")
print(timestamp[0])
