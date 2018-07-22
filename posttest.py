#!/usr/bin/env python
# encoding=utf-8
import requests
import json
getcontrol_url = 'http://smartdp.applinzi.com/php/getcontrol.php'   # 轮询命令

postwind_url = 'http://smartdp.applinzi.com/php/postwind.php'
posttemp_url = 'http://smartdp.applinzi.com/php/posttemphumintens.php'
postcurtain_url = 'http://smartdp.applinzi.com/php/postcurtain.php'
postpump_url = 'http://smartdp.applinzi.com/php/postpump.php'
postdebug_url = 'postdebug.php'

# postwind风机
# wenddata = {
#     'time': '1',
#     'state': '1'
# }
# response = requests.post(base_url, data=winddata)
# -------------------------------------------------------

# # 轮询命令
# r_getcontrol = requests.get(getcontrol_url)
# print "controltext"
# print (r_getcontrol.text[0:2])
# commend = r_getcontrol.text[0:2]
# # --------------------------------------------------------

for i in range(5):  # type: int
    hum = '50'    # type: str
    hum = int(hum)
    temp = 25   # type: str
    intens = 500    # type: str
    print type(hum)
    print repr(hum)
    # posttemp温湿度光照
    posttemp_data = {
        'hum': hum,
        'temp': temp,
        'intens': intens,
        'time': i
    }
    r_posttemp = requests.post(posttemp_url, data = posttemp_data)
    print i
    print "success?"
    print r_posttemp.text
# -------------------------------------------------------

# # 窗帘
# postcurtain_data = {
#     'time':' ',
#     'state':repr(curtain_state)
# }
# r_postcurtain = requests.post(postcurtain_url, data = postcurtain_data)
# # -------------------------------------------------------

# # 水泵
# postpump_data = {
#     'time':' ',
#     'state':repr(pump_state)
# }
# r_postpump = requests.post(postpump_url, data = postpump_data)
# # -------------------------------------------------------
