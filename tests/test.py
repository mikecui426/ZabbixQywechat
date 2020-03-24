#!/usr/bin/python
# -*- coding: utf-8 -*-

from Qywechat import Qywechat
import sys

Agentid="1000002"
Corpid="1111"
Corpsecret="2222"
PATH="/tmp/test.json"

if __name__ == '__main__':
    Touser=sys.argv[1]
    Subject=str(sys.argv[2])
    Content=str(sys.argv[3])
    Result=Qywechat(Agentid,Corpid,Corpsecret,PATH)
    Result.SendMSGtoWechat(Touser,Subject,Content)
