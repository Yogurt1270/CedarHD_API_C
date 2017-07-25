#!/usr/local/bin/python env
# coding:utf-8

import requests


def gettoken():
    url = "https://functest.junhuahomes.com/imapi/user/checkNum"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentCommunityId": "",
        "currentVer": "3.0.0",
        "dscd": "",
        "Login": "",
        "mobile": "13718591270",
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS",
        "validatecode": "1234",
        "xgToken": "191e35f7e0731cc5080"
    }
    req = requests.post(url, data=para, verify=False)
    # print(req.headers['login'])
    return req.headers['login']
