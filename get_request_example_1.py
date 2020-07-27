import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

# send get request
response = requests.get(url)
print(response) # <Response [200]>

# display response content
# print(response.content)
# print(response.headers)

# parse to json format
json_response = json.loads(response.text)
#print(json_response)

# fetch value using jsonpath
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert pages[0] == 5
