#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 8000))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
a='孙国栋'.encode()
for data in [a, b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()