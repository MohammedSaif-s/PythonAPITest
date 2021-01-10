import json
import requests

host_url = 'http://localhost:3000'
#parms = {'id':3}    #to retrieve the specific id from the json file
#response_code = requests.get(host_url + '/users', params=parms)
response_code = requests.get(host_url + '/users')
print('The result of this GET request is: ')
print(response_code)
print(response_code.headers)
print(response_code.headers['Content-type'])
print(response_code.cookies)

result_code = (json.dumps(response_code.json(),indent=4))
print(result_code)