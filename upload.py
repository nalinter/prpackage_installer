import requests

def upload_package(url , access_code ,pkg_path) :

   path = "rest/v11_8/Administration/packages"
   payload = {}
   files = [
      ('upgrade_zip', open(pkg_path,'rb'))
   ]
   headers = {
     'OAuth-Token': access_code
   }
   url_path = url + '/' +path

   file_install_hash = None
   unfile_hash = None
   response = requests.request("POST", url_path, headers=headers, data = payload, files = files)
   print(response)
   response_json = response.json()
   if response.status_code == 200 :
      print("Success ,Uploaded the Package")
      file_install_hash = response_json["file_install"]
      unfile_hash = response_json["unFile"]
      return file_install_hash ,unfile_hash
   else :
      print("Error in Uploading the file")
      print("Status Code : ", response.status_code)
      print("Reason :" ,response_json)
   
   return file_install_hash ,unfile_hash
