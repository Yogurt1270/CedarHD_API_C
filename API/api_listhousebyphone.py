#!/usr/local/bin/python
# coding:utf-8

from Public.gettoken import gettoken
import requests
import json


def listhousebyphone(userphone):
    url = "https://functest.junhuahomes.com/imapi/house/listHouseByPhone"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentCommunityId": "",
        "currentVer": "3.0.0",
        "pageNum": "1",
        "login": gettoken(),
        "userPhone": userphone,
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS",
        "numPerPage": "100"
    }
    req = requests.post(url=url, data=para, verify=False)
    listHouse_res = json.loads(req.text)
    # print(listHouse_res['recordList'][2]['assetId'])
    return listHouse_res
