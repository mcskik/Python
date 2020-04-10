import requests

import ApiJsonPlaceholder.JsonPlaceholder_ApiConstants
import OutputHelper

apiMethod = 'users'
queryString = ''
url = ApiJsonPlaceholder.JsonPlaceholder_ApiConstants.apiEndpoint + apiMethod + queryString
response = requests.get(url)
json_data = response.json()
OutputHelper.viewJsonOutput("JsonPlaceholder_Get_Users", "json", json_data)
