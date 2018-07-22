#!/usr/bin/env python
# encoding=utf-8
import requests
import json
getcontrol_url = 'http://smartdp.applinzi.com/php/getcontrol.php'   # 轮询命令

postwind_url = 'http://smartdp.applinzi.com/php/postwind.php'
posttemp_url = 'http://smartdp.applinzi.com/php/posttemphumintens.php'
postcurtain_url = 'http://smartdp.applinzi.com/php/postcurtain.php'
postpump_url = 'http://smartdp.applinzi.com/php/postpump.php'
postdebug_url = 'http://smartdo.applinzi.com/php/postdebug.php'


# posttemp温湿度光照
def sendtemp(hum, temp, intens):
    posttemp_data = {
        'hum': hum,
        'temp': temp,
        'intens': intens,
        'time': '0'
    }
    r_posttemp = requests.post(posttemp_url, data=posttemp_data)
    return "send ok"
# -------------------------------------------------------

# 轮询命令
def getcommend():
    r_getcontrol = requests.get(getcontrol_url)
    # print "controltext"
    # print (r_getcontrol.text[0:2])

    # commend = [hex(int(c)) for c in r_getcontrol.text[0:2]]
    # commend = hex(ord(str(r_getcontrol.text[0:2]).encode("utf-8")))
    commend = [int(hex(ord(unicode(c).encode('utf-8'))),16) for c in r_getcontrol.text[0:2]]
    # print "type of commend[0])"
    # print type(commend[0])
    return commend
# --------------------------------------------------------


# 窗帘
def sendstate(curtain_state, pump_state):
    postcurtain_data = {
        'time':'0',
        'state':curtain_state
    }
    r_postcurtain = requests.post(postcurtain_url, data = postcurtain_data)
    # -------------------------------------------------------

    # 水泵
    postpump_data = {
        'time':'0',
        'state':pump_state
    }
    r_postpump = requests.post(postpump_url, data = postpump_data)
# -------------------------------------------------------
