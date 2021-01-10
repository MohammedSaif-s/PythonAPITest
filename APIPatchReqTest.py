import requests
import json
host_url = 'http://localhost:3000'
body = {
    "subjectId":3
}
resp_code = requests.patch(host_url +'/users/3',data = body)
print(resp_code)
res_result = (json.dumps(resp_code.json(),indent=4))
print(res_result)