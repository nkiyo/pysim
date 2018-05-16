#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
    return line1

line1 = get_and_clear_line1()
print('line1 is ' + line1 + '.')

