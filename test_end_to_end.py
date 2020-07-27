import requests
import json
import jsonpath

def test_end_to_end():
    url = "http://thetestingworldapi.com/api/studentDetails"
    file = open("/Users/ajayvidekar/Desktop/RESUME/add_user.json", "r")
    request_json = json.loads(file.read())
    response = requests.post(url, request_json)
    # fetch id generated
    id = jsonpath.jsonpath(response.json(), "id")
    print(id[0])
    file.close()

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open("/Users/ajayvidekar/Desktop/RESUME/technical_skills.json", "r")
    request_json = json.loads(file.read())
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    add_api_url = "http://thetestingworldapi.com/api/addresses"
    file = open("/Users/ajayvidekar/Desktop/RESUME/technical_skills.json", "r")
    request_json = json.loads(file.read())
    response = requests.post(tech_api_url, request_json)
    print(response.text)




