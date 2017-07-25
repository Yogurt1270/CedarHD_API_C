#!/usr/local/bin/python env
# coding:utf-8

from Public.gettoken import gettoken
import json
import requests


# 评价列表
def evaluationlist(repairstatus):
    url = "https://functest.junhuahomes.com/imapi/homeRepair/listHomeAndPublicRepairByPage"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentVer": "3.0.0",
        "isComment": "0",
        "numPerPage": "15",
        "pageNum": "1",
        "login": gettoken(),
        "phoneName": "iPhone",
        "platform": "ios",
        "repairType": "",
        "platformVersion": "10.3.2",
        "repairStatus": repairstatus,
        "system": "iOS",
    }
    req = requests.post(url=url, data=para, verify=False)
    res = json.loads(req.text)
    print(res)
    return res
