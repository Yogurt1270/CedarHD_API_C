#!/usr/local/bin/python env
# coding:utf-8

from Public.gettoken import gettoken
import requests
import json


# 获取订单详情
def orderdetail(orderid):
    url = "https://functest.junhuahomes.com/imapi/homeRepair/getDetailByOrderId"
    para = {
        "login": gettoken(),
        "orderId": orderid
    }
    req = requests.post(url=url, data=para, verify=False)
    res = json.loads(req.text)
    print(res)
    return res
