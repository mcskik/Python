import requests

from PostmanEcho import PostmanEcho_ApiConstants

import OutputHelper

# This API simply echos the request you make back as a response.
apiMethod = 'get'
queryString = '?id=789&person_type=777'
url = PostmanEcho_ApiConstants.apiEndpoint + apiMethod + queryString
response = requests.get(url, auth=(PostmanEcho_ApiConstants.authUsername, PostmanEcho_ApiConstants.authPassword))
print(response.text)
json_response_data = response.json()
# responseId = json_response_data['data'][0]['id']  # [0] used to point to a specific element of an array.
responseId = json_response_data['args']['id']
responsePersonType = json_response_data['args']['person_type']
print("Id         = " + str(responseId))
print("PersonType = " + str(responsePersonType))
OutputHelper.viewJsonOutput("PostmanEcho_Get_Sample_With_Auth", "json", json_response_data)
