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
#   Modify:     21.08.2022 01:15        #
# # # # # # # # # # # # # # # # # # # # #

from functions import *
import vk_request
import read_write

app_ids = read_write.readAppids()
print(sign_app_url(app_ids[0]))
json_request = vk_request.vk_api_request(methods['getImageList'],app_ids[0],input())


print(json_request)