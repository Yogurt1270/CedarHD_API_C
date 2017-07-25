#!/usr/local/bin/python env
# coding:utf-8

import requests
import json


def checknum(userphone):
    url = "https://functest.junhuahomes.com/imapi/user/checkNum"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentCommunityId": "",
        "currentVer": "3.0.0",
        "dscd": "",
        "Login": "",
        "mobile": userphone,  # 需要进行参数化处理,读取数据库用户表
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS",
        "validatecode": "1234",
        "xgToken": "191e35f7e0731cc5080"
    }
    req = requests.post(url=url, data=para, verify=False)
    checknum_res = json.loads(req.text)
    # print(checknum_res)
    return checknum_res
