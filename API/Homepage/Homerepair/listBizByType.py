#!/usr/local/bin/python env
# coding:utf-8

import requests
import json

class TestListBytype:
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


    def test_listBizByType(self):
        url = "https://functest.junhuahomes.com/imapi/biz/listBizByType"
        para= {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "login": self.token(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairType": "HOME_REPAIR",
            "system": "iOS"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        print([0]['bizId'])
        return ([0]['bizId'])

# def commitHomeRepair(self):
#     url = 'https://functest.junhuahomes.com/imapi/homeRepair/commitHomeRepair?login=585a768ddfc84b3f961dc9b40e96c87a'
#
