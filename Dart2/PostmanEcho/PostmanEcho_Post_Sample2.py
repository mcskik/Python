import json

import requests

import PostmanEcho.PostmanEcho_ApiConstants

import OutputHelper

apiMethod = 'post/'
personId = 456
personTypeId = 88
url = PostmanEcho.PostmanEcho_ApiConstants.apiEndpoint + apiMethod
json_request_data = {"id": str(personId), "university_undergraduate": True, "sixth_form_pupil": True, "high_school_pupil": True, "person_type": str(personTypeId)}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, headers=headers, data=json.dumps(json_request_data))
print(response.text)
json_response_data = response.json()
# responseId = json_response_data['data'][0]['id']  # [0] used to point to a specific element of an array.
responseId = json_response_data['data']['id']
responsePersonType = json_response_data['data']['person_type']
print("Id         = " + str(responseId))
print("PersonType = " + str(responsePersonType))
OutputHelper.viewJsonOutput("PostmanEcho_Post_Sample2", "json", json_response_data)
