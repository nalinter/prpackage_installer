import requests


def uninstall_pkg_api(url , access_token ,id_hash) :

   path = "rest/v11_8/Administration/packages/" + id_hash + "/uninstall"
   payload = {}
   headers = {
      'OAuth-Token': access_token
   }
   print(id_hash)
   url_path = url + '/' + path
   response = requests.request("GET", url_path, headers=headers, data = payload)
   #response_json = response.json()
   if response.status_code == 200 :
      print("Success ,Package uninstalled")
   else :
      print("Error in uninstalling the package")
      print("Status Code :", response.status_code)
      print("Reason : ", response.json())
       

   
