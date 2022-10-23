# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module main.py writed               #
#       by Niyaz                        #
#   description:                        #
#       the main place of code          #
#       execution. Starts the server    #
#       and manages all the modules     #
#                                       #
#   Created:    21.08.2022 00:45        #
#   Modify:     23.10.2022 11:29        #
# # # # # # # # # # # # # # # # # # # # #

import sys
from functions import *
import vk_request
import read_write
import args

app_ids = []

arg = args.Args()

arg.args()
app_ids = arg.app_ids

if(not arg.not_use_auto_appids):
    app_ids = read_write.readAppids()

if(len(app_ids)<=0):
    print("appids not found or not valid. Program close!")
    quit()

print(sign_app_url(app_ids[0]))
print('введи ссылку с токеном, которую получил: ')
data = get_data_from_url(input())
someid = []
json_request = vk_request.vk_api_request(methods['getImageList'],app_ids[0],data['access_token'])
#print(json_request)
try:
    if(json_request['error']['error_code'] == 5):
        print(json_request['error']['error_msg'])
        quit()
    else:
        print(json_request)
except KeyError as e:
    pass
for i in range(0,json_request['response']['count']):
    someid.append(json_request['response']['items'][i]['id'])
    print(str(json_request['response']['items'][i]['id'])+" : " + json_request['response']['items'][i]['name'])
print("Что ты выбрал?")
select = input()
if(select.isdecimal()):
    responce = vk_request.vk_api_set_Image(methods['setImage'],app_ids[0],data['access_token'],select)
    if(responce['response'] == 1):
        print("ты удачно установил эмоджи статус '"+ json_request['response']['items'][someid.index(int(select))]['name']+"'")
else:
    print("print please a digit from list")