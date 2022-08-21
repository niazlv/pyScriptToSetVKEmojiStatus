# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module functions.py writed          #
#       by Niyaz                        #
#   description:                        #
#       module for any functions        #
#   Created:    21.08.2022 00:48        #
#   Modify:     21.08.2022 01:15        #
# # # # # # # # # # # # # # # # # # # # #

import vk_request

methods={
    'getImageList':'status.getImageList',
    'getImage':'status.getImage',
    'setImage':'status.setImage'
}

def sign_app_url(app_id)->str:
    return('https://oauth.vk.com/authorize?client_id='+str(app_id)+'&scope=1024&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1 \n')

def is_token_valid(token:str)->bool:
    if(not len(token)==198):
        return False
    else:
        return True

def is_appid_valid(appid)->bool:
    r = vk_request._post(sign_app_url(appid))
    if(r.status_code == 200):
        return True
    elif(r.status_code == 401):
        return False
    print(r.text)
    return True

def get_data_from_url(tokenUrl:str)->list[str]:
    data = {
        'access_token':'',
        'expires_in':'',
        'user_id':''
    }
    offset = tokenUrl.find('access_token=')
    if(not offset == -1):
        token = tokenUrl[offset+13 :]
        offset = token.find('&')
        if(not offset == -1):
            token = token[:offset]
        data['access_token'] = token

        offset = tokenUrl.find('expires_in=')
        if(not offset == -1):
            expires_in = tokenUrl[offset+11:]
            offset = expires_in.find('&')
            if(not offset == -1):
                expires_in = expires_in[:offset]
        data['expires_in'] = expires_in

        offset = tokenUrl.find('user_id=')
        if(not offset == -1):
            user_id = tokenUrl[offset+8:]
            offset = expires_in.find('&')
            if(not offset == -1):
                user_id = user_id[:offset]
        data['user_id'] = user_id
    else:
        if(is_token_valid(tokenUrl)):
            data['access_token'] = tokenUrl
    return data
