#!/usr/local/bin/python env
# coding:utf-8


from API.Order.api_listHomeAndPublicRepairByPage import evaluationlist


# 获取待评价列表
def test_evaluationlist():
    res = evaluationlist("")
    print(res)
    assert res['numPerPage'] == 15


# 获取待评价列表
def test_evaluation_abnormal():
    res = evaluationlist("COMPLETED")
    print(res)
    assert res['numPerPage'] == 15
