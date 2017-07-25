#!/usr/local/bin/python env
# coding:utf-8

from Public.gettoken import gettoken
import requests
import json

# 获取未缴清费用列表
def unpay(houseid, paymentType):
    url = "https://functest.junhuahomes.com/imapi/fee/getUnpaidBill"
    para = {
        "login": gettoken(),
        "houseID": houseid,
        "paymentType": paymentType,
        "shouldChargeDateStart": "",
        "shouldChargeDateEnd": "",
        "apiVersion": "1.3.0"
    }
    req = requests.post(url, data=para, verify=False)
    print(req.headers['Set-cookie'])
    unpay_res = json.loads(req.text)
    # print(unpay_res)
    return unpay_res


# 获取可预缴费用列表
def prepay():
    url = "https://functest.junhuahomes.com/imapi/fee/getUnpaidBill"
    para = {
        "login": gettoken(),
        "houseID": "16697",
        "paymentType": "ADVANCE",
        "shouldChargeDateStart": "",
        "shouldChargeDateEnd": "",
        "apiVersion": "1.3.0"
    }
    req = requests.post(url, data=para, verify=False)
    prepay_res = json.loads(req.text)
    # print(prepay_res)
    # print(prepay_res)
    return prepay_res


# 按起止时间获取未缴清费用列表
def prepaybydate():
    url = "https://functest.junhuahomes.com/imapi/fee/getUnpaidBill"
    para = {
        "login": gettoken(),
        "houseID": "16697",
        "paymentType": "COMMON",
        "shouldChargeDateStart": "2017-07",
        "shouldChargeDateEnd": "2017-08",
        "apiVersion": "1.3.0"
    }
    req = requests.post(url, data=para, verify=False)
    bydate_res = json.loads(req.text)
    # print(bydate_res)
    return bydate_res
