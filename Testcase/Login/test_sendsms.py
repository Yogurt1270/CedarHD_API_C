#!/usr/local/bin/python
# coding:utf-8

from API.Login.api_sendchecksms import sendsms


# 获取短信验证码
def test_sendsms():
    res = sendsms("13718591270", "")
    print(res)
    assert res['resultMsg'] == "验证码已发送"


# 获取语音验证码
def test_sendvoicesms():
    res = sendsms("13718591270", "1")
    print(res)
    assert res['resultCode'] == "True"


# 异常值获取验证码
def test_sendexcept():
    res = sendsms("137185912701", "null")
    print(res)
    assert res['message'] == "服务器开小差啦 >_< 稍后再试"
