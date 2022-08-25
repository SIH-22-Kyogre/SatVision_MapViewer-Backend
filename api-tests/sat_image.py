import requests
import os
import json

ENDPOINT = "http://localhost:5000/api/fetch"


# headers = {
#     'Content-type': 'application/json', 
#     'Accept': 'text/plain'
# }
response = requests.post(
    ENDPOINT
)
print("requested")
print(response.content)

