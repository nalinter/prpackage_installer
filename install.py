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
    print(response)
    if response.status_code == 200 :
      print("Success ,Package has been installed")
      return response.status_code
    else :
      print("Error in Installing the package")
      print("Status Code :", response.status_code)
      print("Reason :", response.json())
      print("Deleting the Package")
      delete_pkg_api( url ,access_code ,unfile_hash)
    return None
