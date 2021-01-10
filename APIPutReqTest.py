import json
import requests
host_url = 'http://localhost:3000'
body = {
    "firstName":"Chattur",
    "lastName":"Kumar",
    "age": 23,
    "city_Name":"Kochi",
    "state_Name":"Kerala",
    "interest_In":"BasketBall",
    "subjectId":4
}
res_code = requests.put(host_url +'/users/4', data=body)
print(res_code)
res_result = (json.dumps(res_code.json(),indent=4))
print(res_result)