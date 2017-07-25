#!/user/local/bin/python
# coding:utf-8

import requests
import json


class TestDemand(object):
    # 用户登录, 获取token信息

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
        self.token = request.headers['login']
        print("token is", self.token)
        return self.token

    # 选择报修类型
    def test_listBizByType(self):
        url = "https://functest.junhuahomes.com/imapi/biz/listBizByType"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "login": self.token,
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairType": "COMMUNITY_COMPLAINT",
            "system": "iOS"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        print(para['login'])
        # print(res[1]['leafList'][0]['bizId'])
        # return res[1]['leafList'][0]['bizId']

    # 提交报修单
    def test_commit(self):
        url = 'https://functest.junhuahomes.com/imapi/homeRepair/commitHomeRepair?' + "login=" + "ed1867ae3aa84bbdae5bb7903813b234"
        para = {
            "repairRemark": "QQ",
            "bizId": "fb8905839ceb43159afcef6cb6faad3e",
            "login": "ed1867ae3aa84bbdae5bb7903813b234",
            "communityId": "22206"
        }
        header = {
            "Content-Type": "multipart/form-data; boundary=Boundary+72E9F8FAA0B4C68A"
        }
        req = requests.post(url, para, verify=False, headers=header)
        res = json.loads(req.text)
        print(res)
        #
        # # 返回报修成功页
        # def test_bookingSuccess(self):
        #     url = "https://functest.junhuahomes.com/imapi/order/bookingSuccess"
        #     para = {
        #         "login": self.token,
        #         "orderId": ""
        #     }
        #     req = requests.post(url, data=para, verify=False)
        #     res = json.loads(req.text)
        #     print(res)
