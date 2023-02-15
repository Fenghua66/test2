import json
import requests
from requests.auth import HTTPBasicAuth
 
api_key = "4ryC1ZBnewpPfmMG"
api_secret = "4iRzF5HbDAlfDPcuTeMRhx7Bg9WXzz9w"


# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

print(auth)

headers = {
#'Authorization': 'Basic ' + api_key,
'Content-Type': 'application/json'
}

limit = 1000
params = {"limit": limit}

url = 'https://api.fivetran.com/v1/connectors/sublet_gab'

response = requests.get(url=url, auth=auth, headers=headers, params=params).json()

print(response.keys())

#test note