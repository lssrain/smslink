import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink

import pytest
import allure
import time
import requests
import warnings
from action.loggers import *

loginfo = Log()


def tokens():
    '''
    获取登录token
    :return:
    '''
    warnings.filterwarnings('ignore')
    url = 'https://sit-hlj.rainbowcn.com/api/v1/dubhe-auth/user/th-idm/login'
    json = {
        "smsCode": "",
        "account": "127458",
        "password": "lss@123456",
        "selfDevice": 0
    }
    # loginfo.info('接口:{},入参:{}'.format(url, json))
    token = requests.post(url, json=json, verify=False)
    # loginfo.info('出参:{}'.format(token.json()))
    # print(token.json()['data']['token'])
    return token.json()['data']['token']


if __name__ == '__main__':
    # tokens()
    pass
