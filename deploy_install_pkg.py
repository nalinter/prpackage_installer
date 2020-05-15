import sys
import json
import os
from access_token import generate_access_token
from upload import upload_package
from install import install_package

# from jenkins second argument as pr number
# from local second argument as package name eg: crmatlas-4047

if __name__ == '__main__':
    try:
        environment = sys.argv[1]
        package_pr_id = sys.argv[2]
        
    except:
        print('Not enough arguments')
    print('Environment:', environment)
    print("PR ID:", package_pr_id)
    
    #if you want to test it from jenkins use line number :20 and comment line numbers :  22 
    #package_file_path = "/var/www/html/prpackages/module_"+ package_pr_id + "_modules_1.zip"

    #if you want to test it from local use line number :25 and comment line number : 22
    package_file_path = os.getcwd() + "/" + package_pr_id +".zip"
    json_path =  os.getcwd() + "/environments.json"
    json_open = open(json_path)
    data_json = json.load(json_open)

    envi_info = data_json[environment]
    url = envi_info["env_url"]
    payload = envi_info["credentials"]

    
    access_token = generate_access_token(url=url, payload=payload)
    
    file_hash, unfile_hash = upload_package(url=url ,access_code=access_token , pkg_path=package_file_path)

    install_package(url, access_code=access_token ,file_install_hash = file_hash ,unfile_hash = unfile_hash)
