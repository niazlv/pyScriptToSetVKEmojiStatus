# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module vk_request.py writed         #
#       by Niyaz                        #
#   description:                        #
#       module for vk requests          #
#   Created:    21.08.2022 00:48        #
#   Modify:     21.08.2022 21:01        #
# # # # # # # # # # # # # # # # # # # # #

import requests
import json

def _post(str, payload={}):
    responce = requests.post(str, params=payload)
    return responce

def vk_api_set_Image(method,ids,access_token,status_id)->dict[str, any]:
    payload = {
        'api_id': str(ids),
        'access_token': access_token,
        'status_id': str(status_id),
        'request_id': '7',
        'method': method,
        'format': 'json',
        'v': '5.103'
    }
    url = "https://api.vk.com/method/"+payload['method']
    r = _post(url,payload)
    return json.loads(r.text)

def vk_api_request(method,ids,access_token)->dict[str, any]:
    payload = {
        'api_id': str(ids),
        'access_token': access_token,
        'request_id': '7',
        'method': method,
        'format': 'json',
        'v': '5.103',
    }
    url = "https://api.vk.com/method/"+payload['method']
    r = _post(url,payload)
    return json.loads(r.text)
# response:
#   count: int
#   items:
#       [
#           id: int
#           name: str
#           images:
#               [
#                   url: str
#                   width: int
#                   height: int
#               ]
#       ]