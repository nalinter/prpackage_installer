import requests


def delete_pkg_api(url , access_token , unfile_hash) :

   path = "rest/v11_8/Administration/packages/" + unfile_hash
   payload = {}
   headers = {
    'OAuth-Token': access_token
   }
   url_path = url + '/' + path
   response_status_code = None
   response = requests.request("DELETE", url_path, headers=headers, data = payload) 
   response_json = response.json()
   if response.status_code == 200 :
       print("Success ,Package has been Deleted")
   else :
       print("Error in Deleting the Package")
       print("Status Code:", response.status_code)
       print("Reason : ",response_json)
    
