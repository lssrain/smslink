import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink

import requests
from action.header import *
from action.loggers import *

def batchno():
    '''
    创建消息时batchNo调用data值
    :return:
    '''
    url = 'https://sit-hlj.rainbowcn.com/api/v1/scrm-message/sms/custom/import/batch-no/get'
    json = {}
    res = requests.post(url, json=json, headers=header(), verify=False)
    # print(res.json()['data'])
    return res.json()['data']


if __name__ == '__main__':
    pass
