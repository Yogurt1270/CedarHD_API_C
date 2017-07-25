#!/usr/local/bin/python
# coding:utf-8


import requests
import json


class TestCommit:
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

    def test_commit(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/commitHomeRepair?" + "login=" + self.token()
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "assetId": "22575",
            "bizId": "d56c79b530254ad396c71744c2853ee3",
            "bookDateStr": "2017-07-19(今天)",
            "channel": "",
            "communityId": '22206',
            "continueOrder": "0",
            "currentVer": "3.0.0",
            # "login": self.token(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairContact": "测试LD哈哈",
            "repairPhone": "13718591270",
            "repairRemark": "通过一个月宝宝遇见你",
            "repairType": "HOME_REPAIR",
            "system": "iOS",
            "time": "17:00~19:00"
            repairRemark    QQ
            bizId    fb8905839ceb43159afcef6cb6faad3e
            login    ed1867ae3aa84bbdae5bb7903813b234
            communityId    22206
        }
        header = {
            "Content-Type": "multipart/form-data; boundary=Boundary+72E9F8FAA0B4C68A"
        }
        req = requests.post(url, para, verify=False, headers=header)
        res = json.loads(req.text)
        print(res)
