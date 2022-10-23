# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module args.py writed               #
#       by Niyaz                        #
#   description:                        #
#       module for any functions        #
#   Created:    23.10.2022 11:41        #
#   Modify:     23.10.2022 11:42        #
# # # # # # # # # # # # # # # # # # # # #

import sys
from functions import is_appid_valid

class Args(object):
    app_ids = []
    not_use_auto_appids=False
    def __init__(self):
        
        pass
    def help(self):
        return """\
usage: 
    python3 {0} [--args]\t#аргументы не обязательны\n
args:
    --app_id / -a [appid] \tИспользовать только этот app_id. Аргумент можно применять несколько раз. Автоматически применяется аргумент -d
    --disable_auto / -d \tОтключает автоматическую подкачку из файла appids.txt
    --help / -h \tПоказать это окно\n
example:
    python3 {0}
    python3 {0} --app_id 51432687
    python3 {0} --app_id 51432687 --app_id 7362610 --app_id 7297191
                    """.format(sys.argv[0])
    def args(self):
        l = len(sys.argv)
        if(l > 1):
            i = 1
            while(i<l):
                _arg = [sys.argv[i][:1],sys.argv[i][1:]]
                _double_arg = [sys.argv[i][:2],sys.argv[i][2:]]
                
                if(_double_arg[0] == '--' and i+1 <l and _double_arg[1] == 'app_id'):
                    arg = sys.argv[i+1]
                    if(arg and is_appid_valid(arg)):
                        self.app_ids.append(arg)
                        print(arg)
                    else:
                        print("is not valid! apids:" +arg)
                    self.not_use_auto_appids = True
                    i+=1
                elif(_arg[0] == '-' and _arg[1] == 'd' or _double_arg[0] == '--' and _double_arg[1] == 'disable_auto'):
                    self.not_use_auto_appids = True
                elif(_arg[0] == '-' and _arg[1] == 'h' or _double_arg[0] == '--' and _double_arg[1] == 'help'):
                    print(self.help())
                    quit()
                else:
                    print('argument incorrect!')
                    quit()
                i+=1
