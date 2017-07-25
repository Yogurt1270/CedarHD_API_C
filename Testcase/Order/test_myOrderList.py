#!/usr/local/bin/python env
# coding:utf-8

from API.Order.api_myOrderList import oderlist


# 获取订单列表全部分类
def test_all_order_list():
    res = oderlist("", "")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表室内报修，全部
def test_HOME_REPAIR_list():
    res = oderlist("HOME_REPAIR", "")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表室内报修，待受理
def test_HOME_REPAIR_WAIT_FOR_PROCESS():
    res = oderlist("HOME_REPAIR", "WAIT_FOR_PROCESS")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表室内报修，处理中
def test_HOME_REPAIR_PROCESSING():
    res = oderlist("HOME_REPAIR", "PROCESSING")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表室内报修，维修完成
def test_HOME_REPAIR_REPAIR_COMPLETED():
    res = oderlist("HOME_REPAIR", "REPAIR_COMPLETED")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表室内报修，订单完成
def test_HOME_REPAIR_COMPLETED():
    res = oderlist("HOME_REPAIR", "COMPLETED")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表公区报修
def test_PUBLIC_REPAIR():
    res = oderlist("PUBLIC_REPAIR", "")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表公区报修, 待受理
def test_PUBLIC_REPAIR_WAIT_FOR_PROCESS():
    res = oderlist("PUBLIC_REPAIR", "WAIT_FOR_PROCESS")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表公区报修, 处理中
def test_PUBLIC_REPAIR_COMPLETED():
    res = oderlist("PUBLIC_REPAIR", "PROCESSING")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表公区报修, 待验收
def test_PUBLIC_REPAIR_WAITFORCHECK():
    res = oderlist("PUBLIC_REPAIR", "WAITFORCHECK")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表公区报修, 订单完成
def test_PUBLIC_REPAIR_COMPLETED():
    res = oderlist("PUBLIC_REPAIR", "COMPLETED")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表通用订单
def test_COMMON_ORDER():
    res = oderlist("COMMON_ORDER", "")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表送件订单
def test_EXPRESS_APPOINTMENT():
    res = oderlist("EXPRESS_APPOINTMENT", "")
    print(res)
    assert res['numPerPage'] == 15


# 获取订单列表寄件订单
def test_EXPRESS_SEND():
    res = oderlist("EXPRESS_SEND", "")
    print(res)
    assert res['numPerPage'] == 15
