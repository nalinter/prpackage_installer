import requests
import json


def generate_access_token(url ,payload):
  
   path = "rest/v11_8/oauth2/token"
   payload = json.dumps(payload)
   headers = {
   'Content-Type': 'application/json'
   }
   response_json = None
   url_path = url + '/' + path
   response = requests.request("POST", url_path, headers=headers, data = payload)
   print(response)
   response_json = response.json()
   if response.status_code == 200 :
      print("Success ,Access Code Generated", response_json['access_token'])
      return response_json['access_token']
   else :
      print("Error in generating the access token\n")
      print("response-status:" ,response.status_code)
      print("Reason :" , response.json())

   return response.json()
