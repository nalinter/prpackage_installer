import requests

url = "http://askashya.rtp.raleigh.ibm.com:8888/federal/"


def staged_pkg_api(url , access_token ,pkg_name) :
    path = "rest/v11_8/Administration/packages/staged/"
    payload = {}
    headers = {
        'OAuth-Token': access_token
    }
    unFile_hash = None
    url_path = url + '/' + path
    response = requests.request("GET", url_path, headers=headers, data = payload)
    response_json = response.json()
    response_list = response_json["packages"]
    length = len(response_list)
    for i in range(length) :
        res_json = response_list[i]
        if res_json['name'] == pkg_name :
            unFile_hash = res_json['unFile']
            break
    
    return unFile_hash
