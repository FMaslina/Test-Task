#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Импортируем библиотеки
import socket
import logging

#   Создаём логгер для записи логов
logging.basicConfig(filename="sample.log", level=logging.INFO)
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)

HOST = "127.0.0.1"
PORT = 65432

try:
    #   Оборачиваем всё для удобства в конструкцию with ... as
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #   Привязываем сокет к адресу
        s.bind((HOST, PORT))
        #   Принимаем подключение
        s.listen()
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        #   В цикле принимаем данные, обрабатываем их, записываем в логи, и отправляем сообщение об успешной отправке
        while True:
            get_data = conn.recv(1024)
            if not get_data:
                break
            get_data = get_data.decode().split()
            logging.info(get_data)
            #   Тут, так и не понял почему, если просто сравнить get_data[-1] == "00", условие не проходит
            if get_data[-1][-1] == "0" and get_data[-1][0] == "0":
                send_data = \
                    f'Спортсмен, нагрудный номер {get_data[0]} прошёл отсечку {get_data[1]} в {get_data[2][0:-2]}'
                print(send_data)
            conn.send('Данные отправлены'.encode())
except BaseException:
    print('Что-то пошло не так!')