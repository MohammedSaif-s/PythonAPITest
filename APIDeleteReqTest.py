import requests
import json
host_url = 'http://localhost:3000'
resp_code = requests.delete(host_url+ '/users/3')
print(resp_code)
res_result = (json.dumps(resp_code.json(),indent=4))
print(res_result)