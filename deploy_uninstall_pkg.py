import sys
import json
import os
from access_token import generate_access_token
from uninstall_pkg import uninstall_pkg_api
from delete_pkg import delete_pkg_api
from installed_pkg import installed_pkg_api
from staged_pkg import staged_pkg_api

# from jenkins second argument as pr number
# from local second argument as package name eg: crmatlas-4047

if __name__ == '__main__':
    envi = sys.argv[1]
    pr_number = sys.argv[2]

#if you want to test it from jenkins use line numbers :18 and comment line numbers : 21
pkg_name =  "module_"+ pr_number + "_modules_1"

#if you want to test it from local use line numbers : 21 and comment line numbers : 18
#pkg_name = pr_number


json_path = os.getcwd() + "/environments.json"
json_open = open(json_path)
data_json = json.load(json_open)

envi_info = data_json[envi]
envi_url = envi_info["env_url"]
envi_payload = envi_info["credentials"]

access_response_token = generate_access_token(envi_url ,envi_payload)

if access_response_token == None :
    exit()

pkg_id = installed_pkg_api(envi_url ,access_response_token ,pkg_name)

if pkg_id == None :
    print("Package doesn't exist")
    exit()
else :
    print("Package already installed.. Deleting the Package")

    uninstall_pkg_api(envi_url ,access_response_token, pkg_id)
    unFile_hash = staged_pkg_api(envi_url ,access_response_token ,pkg_name)

    if unFile_hash == None :
        print("There is no package to be Uninstall")
        exit()
    else :
        delete_pkg_api(envi_url ,access_response_token ,unFile_hash)



