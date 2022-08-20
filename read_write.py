# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module read_write.py writed         #
#       by Niyaz                        #
#   description:                        #
#       module reads/writes data on     #
#       the device                      #
#   Created:    21.08.2022 00:48        #
#   Modify:     21.08.2022 00:56        #
# # # # # # # # # # # # # # # # # # # # #
def readAppids()->list[str]:
    app_ids=['7362610']
    try:
        with open('appids.txt', 'r') as f:
            app_ids = f.read().splitlines()
    except Exception as e:
        print(e)
    return(app_ids)
print(readAppids())