#!/usr/local/bin/python env
# coding:utf-8

from Public.gettoken import gettoken

import requests
import json


# 获取订单列表
def oderlist(repairstatus, repairtype):
    url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentVer": "3.0.0",
        "numPerPage": "15",
        "pageNum": "1",
        "login": gettoken(),
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "repairStatus": repairstatus,
        "repairType": repairtype,
        "system": "iOS",
    }
    req = requests.post(url, data=para, verify=False)
    res = json.loads(req.text)
    print(res)
    return res
