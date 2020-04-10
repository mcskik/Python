import requests

import OutputHelper
from AndroidVersionsService import AndroidVersionsService_ApiConstants

apiMethod = 'android/jsonarray'
queryString = ''
url = AndroidVersionsService_ApiConstants.apiEndpoint + apiMethod + queryString
response = requests.get(url)
json_data = response.json()
OutputHelper.viewJsonOutput("AndroidVersionsService_Get_List", "json", json_data)
