#!/usr/local/bin/python
# coding:utf-8

import requests
import json


def listHouseByPhone():
    url = "https://functest.junhuahomes.com/imapi/house/listHouseByPhone"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentCommunityId": "",
        "currentVer": "3.0.0",
        "pageNum": "1",
        "login": "",
        "mobile": "13718591270",
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS",
        "numPerPage": "100"
    }
    req = requests.post(url=url, data=para, verify=False)
    res = json.loads(req.text)
    print(res['recordList'][0]['assetName'])


listHouseByPhone()
