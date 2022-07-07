#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Импортируем библиотеки
import socket
from random import randint

HOST = "127.0.0.1"
PORT = 65432

try:
    #   Оборачиваем всё для удобства в конструкцию with ... as
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #   Подключаемся по хосту и порту
        s.connect((HOST, PORT))
        #   В цикле, в каждой итерации создаем случайные значения, отправляем их, и получаем сообщение от сервера
        for i in range(100):
            bbbb = str(randint(0, 9999)).zfill(4)
            nn = str(randint(0, 99)).zfill(2)
            hh = str(randint(1, 24)).zfill(2)
            mm = str(randint(0, 60)).zfill(2)
            ss = str(randint(0, 60)).zfill(2)
            zhq = str(randint(0, 999)).zfill(3)
            gg = str(randint(0, 10)).zfill(2)
            send_data = f'{bbbb} {nn} {hh}:{mm}:{ss}.{zhq} {gg}\r'.encode()
            s.send(send_data)
            get_data = s.recv(1024)
            print(f'{get_data.decode()}')
except BaseException:
    print('Что-то пошло не так!')