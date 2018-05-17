#!/usr/bin/python3
# -*- coding: utf-8 -*-
# see => https://qiita.com/msrks/items/0550603efc59f6e8ba09
import socket
from datetime import datetime
from time import sleep

s = socket.socket()

port = 5000
s.bind(('', port))

while True:
    print('listening...')
    s.listen(5)
    c, addr = s.accept()
    #print('receiving from ...')
    print("received ", c.recv(4096))
    while True:
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        try:
            print('send: ', now)
            c.send(bytes(now, encoding='utf-8'))
            print("recv: ", c.recv(4096).decode("utf-8"))
        except:
            break
        sleep(1)
    c.close()
s.close()

