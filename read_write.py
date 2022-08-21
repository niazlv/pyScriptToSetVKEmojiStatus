# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module read_write.py writed         #
#       by Niyaz                        #
#   description:                        #
#       module reads/writes data on     #
#       the device                      #
#   Created:    21.08.2022 00:48        #
#   Modify:     21.08.2022 04:14        #
# # # # # # # # # # # # # # # # # # # # #

# read data from file appids.txt and return readed data as list[str]
def readAppids()->list[str]:
    app_ids=['7362610'] #std app on emoji. Will always exist
    try:
        with open('appids.txt', 'r') as f:
            app_ids = f.read().splitlines()
    except Exception as e:
        print(e)
    return(app_ids)

def writeAppids(appids:list[str])->bool:
    try:
        with open('appids.txt','w') as f:
            for i in range(0,len(appids)):
                f.write(appids[i]+'\n')
    except Exception as e:
        print(e)
        return False
    return True

def appendAppid(appid)->bool:
    try:
        with open('appids.txt','r+') as f:
            r = f.read().splitlines()
            f.write(str(appid)+'\n')
    except Exception as e:
        print(e)
        return False
    return True

def removeAppid(appid)->bool:
    try:
        with open('appids.txt','r+') as f:
            app_ids = f.read().splitlines()
    except Exception as e:
        print(e)
        return False
    try:
        app_ids.remove(appid)
        writeAppids(app_ids)
    except ValueError as e:
        #print(e)
        return False
    return True