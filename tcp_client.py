#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 参考URL: socket => https://qiita.com/msrks/items/0550603efc59f6e8ba09
# 参考URL: logging => https://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
import socket
from contextlib import closing
import sys
import signal
import logging
import re

# ファイル1行目の文字列を取得し、ファイルから削除する
def get_and_clear_line1():
    read_file = 'send_msg.txt'
    write_file = 'new_send_msg.txt' # for debug
    # write_file = read_file

    # ファイル内容を読み込む
    file = open(read_file)
    lines = file.readlines()
    file.close()

    # ファイル内容を書き出す。1行目だけは削除する。
    with open(write_file, 'w', encoding = 'utf-8') as myfile:
        line1 = lines[0]
        print('line1:', line1)
        lines[0] = '\n'
        myfile.write(''.join(lines))
    return line1.rstrip()

# 接続先(TCPサーバ)
host = sys.argv[1]
port = 5000

# ログの設定
logging.basicConfig(filename="comm.log",
                            filemode='a',
                            format='%(asctime)s.%(msecs)03d%(levelname)s %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S',
                            level=logging.DEBUG)

logging.info("============== START ==============")

#with closing(s):
s = socket.socket()
s.connect((host, port))
# TODO 不要
init_msg = "hi"
s.send(bytes(init_msg, encoding='utf-8'))
logging.info("send: %s" % (init_msg))

try:
    while True:

        # メッセージ受信
        recvbin = s.recv(4096)
        recvstr = recvbin.decode("utf-8")
        print ("recvbin: ", recvbin)
        print ("recv: ", recvstr)
        logging.info("%s: %s" % ("recv", recvstr))

        # 受信した時刻の秒数が偶数か奇数かにより、返信するメッセージを変更
        #m = re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:(?P<sec>\d{2})', recvstr)
        #sec = int(m.group('sec'))
        #if (sec % 2)  == 0:
        #    sendstr = str(sec) + " is even."
        #else:
        #    sendstr = str(sec) + " is odd."
        # 送信する文字列を、ファイルから取得する
        sendstr = get_and_clear_line1()
        # TODO sendstrが空文字なら送信しない

        # メッセージ送信
        sendbin = bytes(sendstr, encoding='utf-8')
        s.send(sendbin)
        print("send: %s" % (sendstr))
        print ("sendbin: ", sendbin)
        logging.info("send: %s" % (sendstr))

# ctrl-c押下によるプログラム停止
except KeyboardInterrupt:
    logging.info("============== END ==============\n\n")
    sys.exit(0)
