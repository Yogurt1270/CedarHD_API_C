#!/usr/local/bin/pthone env
# coding:utf=8

import requests
import json


class TestRefreshUser:
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
        return token

    # 未认证用户
    def test_refreshuser(self):
        url = "https://functest.junhuahomes.com/imapi/house/refreshUserIdentity"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "houseId": "113182",
            "login": self.token(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "userPhone": "13718591270"
        }
        req = requests.post(url, para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert 'status' == 'NO_VERIFY'

# 已认证用户
    def test_refreshuser(self):
        url = "https://functest.junhuahomes.com/imapi/house/refreshUserIdentity"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "houseId": "113182",
            "login": self.token(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "userPhone": "13718591270"
        }
        req = requests.post(url, para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert 'status' == 'NO_VERIFY'
