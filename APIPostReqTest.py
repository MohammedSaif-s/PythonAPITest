import json
import requests

host_url = 'http://localhost:3000'
body = {
    "firstName":"Rajeev",
    "lastName":"Kumar",
    "age":24,
    "city_Name":"Hyderabad",
    "state_Name":"Telangana",
    "subjectId":4
    }
resp_code = requests.post(host_url + '/users', data = body)
print(resp_code)
resp_result = (json.dumps(resp_code.json(),indent=4))
print(resp_result)