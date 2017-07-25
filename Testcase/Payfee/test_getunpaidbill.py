#!/usr/local/bin/python env
# coding:utf-8

from API.api_checknum import checknum
from API.api_logout import logout
from API.api_listhousebyphone import listhousebyphone
from API.api_getunpaidbill import unpay


# 获取默认地址的房屋ID
def setup():
    print("------Test start------")


def teardown():
    logout()
    print("------Test end------")


# 获取未缴清费用列表
def test_getbill_001():
    houseid = listhousebyphone(13718591270)['recordList'][2]['assetId']
    paymentType = "COMMON"
    # unpay(houseid, paymentType)
    assert unpay(houseid, paymentType)['houseID'] == houseid


# 获取可预缴费用列表
def test_getbill_002():
    houseid = listhousebyphone(13718591270)['recordList'][2]['assetId']
    paymentType = "ADVANCE"
    print(unpay(houseid, paymentType))
    assert unpay(houseid, paymentType)['houseID'] == houseid
