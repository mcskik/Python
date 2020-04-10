import requests

import ApiJsonPlaceholder.JsonPlaceholder_ApiConstants
import OutputHelper

apiMethod = 'users'
# This API method accepts the id parameter in two formats:
# either as a normal query string parameter like: ?id=1
# or as an additional path folder parameter like: /1
queryString = '?id=1'
# queryString = '/1'
url = ApiJsonPlaceholder.JsonPlaceholder_ApiConstants.apiEndpoint + apiMethod + queryString
response = requests.get(url)
json_data = response.json()
OutputHelper.viewJsonOutput("JsonPlaceholder_Get_User", "json", json_data)
