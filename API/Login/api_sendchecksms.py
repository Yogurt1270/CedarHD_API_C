#!/usr/local/bin/python env
# coding:utf-8

from Public.gettoken import gettoken
import requests
import json


# 发送验证码接口
# isvoice=1语音验证码
def sendsms(userphone, isvoice):
    url = "https://functest.junhuahomes.com/imapi/user/sendCheckSms"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentVer": "3.0.0",
        "login": gettoken(),
        "mobile": userphone,
        "isVoice": isvoice,
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS"
    }
    req = requests.post(url, data=para, verify=False)
    res = json.loads(req.text)
    print(res)
    return res
