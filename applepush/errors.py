#!/usr/bin/env python
#coding:utf-8
"""
  Author:  dog - <yafeile@sohu.com>
  Purpose: 
  Created: 2016年12月06日
"""

REASON = dict(
    BadCollapseId="推送的消息超出最大允许的大小",
    BadDeviceToken="推送的Token不合法",
    BadExpirationDate="推送过期时间不合理",
    BadMessageId="apns-id有问题",
    BadPriority="apns-priority有问题",
    BadTopic="apns-topic不合法",
    DeviceTokenNotForTopic="设备Token与Topic不匹配",
    MissingTopic="没有提供Topic",
    PayloadEmpty="推送内容为空",
    TopicDisallowed="提送的Topic不允许",
    BadCertificate="证书有问题",
    BadCertificateEnvironment="推送的证书推送的环境不对",
    ExpiredProviderToken="设备Token已经过期",
    DuplicateHeaders="请求头重复",
    IdleTimeout="超时",
    MissingDeviceToken="没有提供设备Token",
    MissingProviderToken="没有提供设备Token或证书",
    Forbidden="对应操作不允许",
    InvalidProviderToken="提供的Token签名不正常",
    BadPath="请求路径不对",
    MethodNotAllowed="请求方法不为POST",
    Unregistered="设备Token不可用",
    PayloadTooLarge="推送的内容太大",
    TooManyProviderTokenUpdates="设备Token更新太快",
    TooManyRequests="相同的设备请求次数过多",
    InternalServerError="推送服务器发生错误",
    ServiceUnavailable="推送服务不可用",
    Shutdown="推送服务器挂了"
)