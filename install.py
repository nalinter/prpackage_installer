import requests
from delete_pkg import delete_pkg_api

def install_package(url , access_code , file_install_hash , unfile_hash) :

    path = "rest/v11_8/Administration/packages/" + file_install_hash + "/install/"
    payload = {}
    headers = {
      'OAuth-Token': access_code
    }
    url_path = url + '/' + path
    response = requests.request("GET", url_path, headers=headers, data = payload)
<<<<<<< HEAD
    print(response)
    response_json = response.json()
=======
    #response_json = response.json()
>>>>>>> 5c6a595bf47e35af0b39ca9d0ce5cbd40bcfd3ea
    response_status_code = None
    if response.status_code == 200 :
      print("Success ,Package has been installed")
      response_status_code =  response.status_code
      return response_status_code
    else :
      print("Error in Installing the package")
      print("Status Code :", response.status_code)
      print("Reason :", response.json())
      print("Deleting the Package")
      delete_pkg_api( url ,access_code ,unfile_hash)
    return response_status_code
