#!/usr/local/bin/python
# coding:utf-8


from Public.gettoken import gettoken
import requests
import json


# 退出登录
def logout():
    url = "https://functest.junhuahomes.com/imapi/user/logout"
    data = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentVer": "3.0.0",
        "login": gettoken(),
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS",
        "xgToken": "191e35f7e0731cc5080"
    }

    r = requests.post(url, data=data, verify=False)
    respon = json.loads(r.text)
    # print(respon)
    return respon
