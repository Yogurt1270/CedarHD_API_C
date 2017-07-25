#!/usr/local/bin/python
# coding:utf-8

from API.Login.api_checkIOSVersion import checkversion


# 新版本更新
def test_newversion():
    res = checkversion("3.0.0")
    print(res)
    assert res['message'] == "已经是最新版本", "新版本更新失败"


# 旧版本更新
def test_oldversion():
    res = checkversion("2.0.0")
    print(res)
    assert res['updatePlan'] == "PROMPT_UPDATE", "新版本更新失败"


# 传入异常值更新
def test_exceptversion():
    res = checkversion("")
    print(res)
    assert res['updatePlan'] == "PROMPT_UPDATE", "新版本更新失败"
