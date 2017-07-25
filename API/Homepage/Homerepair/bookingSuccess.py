#!/usr/local/bin/python
# coding:utf-8


import requests
import json

class Testbooking:
    def token(self):
        url = "https://functest.junhuahomes.com/imapi/user/checkNum"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentCommunityId": "",
            "currentVer": "3.0.0",
            "dscd": "",
            "login": "",
            "mobile": "13718591270",
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "validatecode": "1234",
            "xgToken": "191e35f7e0731cc5080"
        }
        request = requests.post(url, data=para, verify=False)
        res = json.loads(request.text)
        token = request.headers['login']
        print(token)
        return token

    def test_booking(self):
        url = "https://functest.junhuahomes.com/imapi/order/bookingSuccess"
        para = {
            "login": self.token(),
            "orderId": "33ce4342501d47e5b338081bc7e24930"
        }
        req = requests.post(url, para, verify=False)
        res = json.loads(req.text)
        print(res['message'])
        assert res['message'] == "恭喜您，报修成功"

