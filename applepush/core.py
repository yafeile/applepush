# coding:UTF-8


"""
基于HTTP2的苹果推送
@author: yubang
创建于2016年11月18日
"""

from hyper import HTTPConnection, tls
from hyper.http20.errors import get_data
from errors import REASON
import json


class ApplePush:
    def __init__(self, cert, apns_topic):
        self.cert = cert
        self.headers = {"apns-topic": apns_topic}
        self.api_url = 'api.development.push.apple.com:443'
        self.api_path = '/3/device/{0}'

    def get_api_path(self, token):
        """
        获取请求的API路径
        :param token:
        :return:
        """
        return self.api_path.format(token)

    @staticmethod
    def make_response(r):
        """
        封装返回对象
        :param r:
        :return:
        """
        data = r.read()
        status = r.status
        if status > 200 and data:
            data = json.loads(data)
            error_msg=data.get('reason', '未知错误')
            return dict(response='推送失败',
                        error_msg=REASON.get(error_msg,'失败'),
                        headers=dict(r.headers))
        else:
            return dict(response='推送成功')

    @staticmethod
    def handle_token(token):
        """
        处理token
        :param token: 苹果设备token
        :return:
        """
        if token.startswith('<'):
            token = token[1:]
        if token.endswith('>'):
            token = token[:-1]
        token = ''.join(token.split())
        return token
    
    def single_push(self, token, alert, badge=1):
        """
            发送单个设备
            :param token:设备ID
            :param alert:弹出的消息内容
            :param badge:显示的消息数量
            :return:
            """
        token = self.handle_token(token)
        payload = {
            'aps': {
                'alert': alert,
                'sound': 'default',
                'badge': badge,
            }
        }
        context = tls.init_context(cert=self.cert)
        conn = HTTPConnection(self.api_url, ssl_context=context)
        try:
            conn.request('POST', self.get_api_path(token), 
                         body=json.dumps(payload), 
                         headers=self.headers)
        except Exception as e:
            return get_data(e)
        else:
            resp = conn.get_response()
            return self.make_response(resp)

    @staticmethod
    def doc():
        print "具体请参考：https://developer.apple.com/library/prerelease/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html#//apple_ref/doc/uid/TP40008194-CH11-SW1"
