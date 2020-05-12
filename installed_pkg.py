import requests

url = "http://askashya.rtp.raleigh.ibm.com:8888/federal/rest/v11_8/Administration/packages/installed"

def installed_pkg_api(url , access_token ,pkg_name) :

    path = "rest/v11_8/Administration/packages/installed"
    payload = {}
    headers = {
        'OAuth-Token': access_token
    }
    id_hash = None
    url_path = url + '/' + path
    response = requests.request("GET", url_path, headers=headers, data = payload)
    response_json = response.json()
    response_list = response_json["packages"]
    length = len(response_list)
    for i in range(length) :
        res_json = response_list[i]
        if res_json['name'] == pkg_name :
            id_hash = res_json['id']
            break
    
    return id_hash