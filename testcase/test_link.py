import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink

import datetime
import requests
from action.header import *
from action.batchno import *
from action.loggers import *
import pytest
import allure

header = header()
loginfo = Log()

@allure.epic('天虹scrm')
@allure.feature('短信-小程序超链')
class Link:

    @allure.title('短信生成小程序超链测试用例')
    @allure.story("结束日期小于未大于当前时间1min")
    def test_addshortdate(self):
        '''
        创建超链，结束日期小于未大于当前时间1min
        :return:
        '''
        end_min = ((datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))
        url = 'http://sit-hlj.rainbowcn.com/api/v1/scrm-message/uri/convert/miniapp/short'
        json = {
            "linkTypeCode": "fixed",
            "miniAppId": 66,
            "params": {
                "pageCode": "maotaiPreorderIndex",
                "pagePath": "index/pages/index/index"
            },
            "expireTime": end_min
        }
        res = requests.post(url, json=json, headers=header, verify=False)
        print(res.json())
        assert res.json()['message'] == '有效期时间与当前时间的间隔必须大于1分钟且小于1年'

    @allure.title('短信生成小程序超链测试用例')
    @allure.story("结束日期小于大于当前时间1year")
    def test_addshortyear(self):
        '''
        创建超链，结束日期小于大于当前时间1year
        :return:
        '''
        end_year = ((datetime.datetime.now() + datetime.timedelta(days=367)).strftime("%Y-%m-%d %H:%M:%S"))
        url = 'http://sit-hlj.rainbowcn.com/api/v1/scrm-message/uri/convert/miniapp/short'
        json = {
            "linkTypeCode": "fixed",
            "miniAppId": 66,
            "params": {
                "pageCode": "maotaiPreorderIndex",
                "pagePath": "index/pages/index/index"
            },
            "expireTime": end_year
        }
        res = requests.post(url, json=json, headers=header, verify=False)
        print(res.json())
        assert res.json()['message'] == '有效期时间与当前时间的间隔必须大于1分钟且小于1年'

    @allure.title('短信生成小程序超链测试用例')
    @allure.story("创建超链")
    def test_addshort(self):
        '''
        创建超链
        :return:
        '''

        end_min = ((datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S"))
        url = 'http://sit-hlj.rainbowcn.com/api/v1/scrm-message/uri/convert/miniapp/short'
        json = {
            "linkTypeCode": "fixed",
            "miniAppId": 66,
            "params": {
                "pageCode": "maotaiPreorderIndex",
                "pagePath": "index/pages/index/index"
            },
            "expireTime": end_min
        }
        res = requests.post(url, json=json, headers=header, verify=False)
        print(res.json())
        assert res.json()['data'] != ''


if __name__ == '__main__':
    # addshort_year()
    pytest.main(['-s', '-q', '--alluredir', './result/allure_xml'])
    os.system(r"allure generate --clean ./result/allure_xml -o ./result/report")
