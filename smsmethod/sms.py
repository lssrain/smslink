import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink

import requests
import pymysql
from action.header import *
from action.batchno import *
from action.loggers import *

header = header()
batchno = batchno()
loginfo = Log()


def addmember():
    '''
    手动推送通过手机号添加发送对象--会员
    :return:
    '''
    url = 'https://sit-hlj.rainbowcn.com/api/v1/scrm-message/sms/custom/card-no/import/add'
    json = {"smsAddToImportRequestList": [
        {"cardNo": "7800100000026612", "level": 3, "mobile": "18320762135", "openId": "", "status": 1,
         "levelName": "金卡"}], "batchNo": batchno}
    res = requests.post(url, json=json, headers=header, verify=False)
    assert res.json()['code'] == 200


def addsms():
    '''
    手动推送添加消息
    :return:
    '''
    addmember()
    url = 'https://sit-hlj.rainbowcn.com/api/v1/scrm-message/sms/custom/update'
    json = {"sendName": "只是一个活动名称", "content": "这是一个短信内容", "sendTime": "", "batchNo": batchno, "signType": "ds",
            "chargeMode": 1, "chargeStore": [{"bdCode": "C001", "regionCode": "C010", "storeCode": "00133"}],
            "userType": "2", "submitCount": 1, "importFileIds": []}
    res = requests.post(url, json=json, headers=header, verify=False)
    # print(res.json())
    assert res.json()['code'] == 200


def runsql():
    '''
    获取消息推送ID--send_id
    :return:
    '''
    db = pymysql.connect(host='192.168.147.192', port=3306, user='scrm_message', password='klFzxPPGYu104C8J',
                         db='scrm_messagedb', charset='utf8')
    cursor = db.cursor()

    cursor.execute(
        "SELECT send_id FROM `sms_custom_send_import_data` WHERE batch_no='1610702413233439d13f6dfe748a5b2519cc5d9e78e2d';")
    for send_id in cursor.fetchall()[0]:
        # print(send_id)
        return send_id


def submit():
    '''
    提交审核
    :return:
    '''
    url = 'https://sit-hlj.rainbowcn.com/api/v1/scrm-message/sms/custom/audit/submit'
    json = {'id': runsql()}
    res = requests.post(url, json=json, headers=header, verify=False)
    # print(res.json())
    assert res.json()['code'] == 200


def audit():
    '''
    审核通过
    :return:
    '''
    submit()
    url = 'https://sit-hlj.rainbowcn.com/api/v1/scrm-message/sms/custom/audit'
    json = {'id': 468, 'auditStatus': 1}
    res = requests.post(url, json=json, headers=header, verify=False)
    # print(res.json())
    assert res.json()['code'] == 200


if __name__ == '__main__':
    audit()
