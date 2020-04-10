import json

import requests

import PostmanEcho.PostmanEcho_ApiConstants

import OutputHelper

apiMethod = 'post/'
personId = 123
personTypeId = 99
url = PostmanEcho.PostmanEcho_ApiConstants.apiEndpoint + apiMethod
json_request_data = {"id": str(personId), "university_undergraduate": True, "sixth_form_pupil": True, "high_school_pupil": True, "person_type": str(personTypeId)}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, headers=headers, data=json.dumps(json_request_data))
print(response.text)
json_response_data = response.json()
data = json_response_data['data']
responseId = data['id']
responsePersonType = data['person_type']
print("Id         = " + str(responseId))
print("PersonType = " + str(responsePersonType))
OutputHelper.viewJsonOutput("PostmanEcho_Post_Sample1", "json", json_response_data)
