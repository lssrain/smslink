import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest
import time
import allure
import requests
import warnings


@pytest.fixture(scope='function', autouse=True)
def token():
    warnings.filterwarnings('ignore')
    url = 'https://sit-hlj.rainbowcn.com/api/v1/dubhe-auth/user/th-idm/login'
    json = {
        "smsCode": "",
        "account": "127458",
        "password": "lss@123456",
        "selfDevice": 0
    }
    token = requests.post(url, json=json, verify=False)
    # print(token.json()['data']['token'])
    return token.json()['data']['token']
