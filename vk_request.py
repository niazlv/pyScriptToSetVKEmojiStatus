# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module vk_request.py writed         #
#       by Niyaz                        #
#   description:                        #
#       module for vk requests          #
#   Created:    21.08.2022 00:48        #
#   Modify:     21.08.2022 01:15        #
# # # # # # # # # # # # # # # # # # # # #

import requests
import json

def _post(str, payload):
    responce=requests.post(str, params=payload)
    return responce

def vk_api_request(method,ids,access_token)->json:
    payload={
    'api_id':ids,
    'access_token':access_token,
    'request_id':'7',
    'method':method,
    'format':'json',
    'v':'5.103',
    }
    url="https://api.vk.com/method/"+payload['method']
    r=_post(url,payload)
    return json.loads(r.text)
# respose:
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