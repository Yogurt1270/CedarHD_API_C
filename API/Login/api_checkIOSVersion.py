#!/usr/local/bin/python
# coding:utf-8

import requests
import json


def checkversion(version):
    requrl = "https://functest.junhuahomes.com/imapi/base/checkIOSVersion"
    para = {
        "Imei": "be7faff4f79bsetupf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentVer": version,
        "Login": "",
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS"
    }
    req = requests.post(url=requrl, data=para, verify=False)
    res = json.loads(req.text)
    # print(res)
    return res
