#!/usr/local/bin/python env
# coding:utf-8

from API.Order.api_GetDetailByOrderId import orderdetail


# 获取订单详情
def test_oderdetail():
    res = orderdetail("33ce4342501d47e5b338081bc7e24930")
    print(res)
    assert res['orderId'] == orderdetail("33ce4342501d47e5b338081bc7e24930")


# 订单编号异常时
def test_orderabnormal():
    res = orderdetail("null")
    print(res)
    assert res['orderId']
