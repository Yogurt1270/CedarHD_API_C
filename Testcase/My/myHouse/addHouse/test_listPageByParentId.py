#!/usr/local/bin/python env
# coding:utf-8

import requests
import json

class TestListPageByParentId:

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
        # self.assertIsNotNone(res['userPhone'], "用户手机号不能为空")
        return token

    # 按parentId返回房屋列表
    def test_listPageByParentId(self):
        url='https://functest.junhuahomes.com/imapi/house/listPageByParentId'
        para={
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "numPerPage": "1",
            "currentVer": "3.0.0",
            "pageNum": "1",
            "login": self.token(),
            "parentId": "105520",
            "phoneName": "测试的iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        # 判断返回的parentName是否与parentId一致
        assert res['recordList'][0]['parentId'] == '105036'
