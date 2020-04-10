import requests

import OutputHelper
from RecipePuppy import RecipePuppy_ApiConstants

apiMethod = 'api'
queryString = '?q=omlette'
url = RecipePuppy_ApiConstants.apiEndpoint + apiMethod + queryString
response = requests.get(url)
json_data = response.json()
OutputHelper.viewJsonOutput("RecipePuppy_Get_Search", "json", json_data)
