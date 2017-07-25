#!/usr/local/bin/python env
# coding:utf-8

from API.api_checknum import checknum
from API.api_logout import logout


def setup():
    print("------test start------")


def teardown():
    print("------test end------")
    logout()


# 使用已认证手机号登录APP
def test_login_001():
    res = checknum(13718591270)
    # print(res)
    assert res['userPhone'] == '13718591270'


# 使用"未认证"手机号登录APP
def test_login_002():
    res = checknum(15901293186)
    # print(res)
    assert res['userPhone'] == '15901293186'


# 使用空手机号
def test_login_003():
    res = checknum("")
    # print(res)
    assert res['message'] == '电话号码不能为空'


# 使用错误的手机号登录APP
def test_login_004():
    res = checknum(1234567890)
    # print(res)
    assert res['userPhone'] == '1234567890'
