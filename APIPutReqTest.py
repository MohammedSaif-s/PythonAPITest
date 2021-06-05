import json
import requests

host_url = 'http://localhost:3000'
body = {
    "firstName":"Rajeev",
    "lastName":"Kumar",
    "age": 24,
    "companyName": "Acer",
    "city_Name": "Hyderabad",
    "state_Name":"Telangana",
    "interest_In":"BasketBall",
    "subjectId":3
}
res_code = requests.put(host_url +'/users/3', data=body)
print(res_code)
res_result = (json.dumps(res_code.json(),indent=4))
print(res_result)