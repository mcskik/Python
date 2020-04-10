import requests

import ApiJsonPlaceholder.JsonPlaceholder_ApiConstants
import OutputHelper

apiMethod = 'comments'
queryString = ''
url = ApiJsonPlaceholder.JsonPlaceholder_ApiConstants.apiEndpoint + apiMethod + queryString
response = requests.get(url)
json_data = response.json()
OutputHelper.viewJsonOutput("JsonPlaceholder_Get_Comments", "json", json_data)
