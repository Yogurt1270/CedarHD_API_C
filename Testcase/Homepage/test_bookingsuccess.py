#!/usr/local/bin/python
# coding:utf-8

from Public.gettoken import gettoken
import requests
import json


def test_booking():
    url = "https://functest.junhuahomes.com/imapi/order/bookingSuccess"
    para = {
        "login": gettoken(),
        "orderId": "33ce4342501d47e5b338081bc7e24930"
    }
    req = requests.post(url, para, verify=False)
    res = json.loads(req.text)
    print(res['message'])
    assert res['message'] == "恭喜您，报修成功"
