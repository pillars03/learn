# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector
import threading
# change root password to yours:
def select():
    conn = mysql.connector.connect(user='root', password='', database='gamemana')
    cursor = conn.cursor()
    cursor.execute('select * from gm_game_tongji where id<200000')
    values = cursor.fetchall()
    cursor.close()
    conn.close()

def select2():
    conn = mysql.connector.connect(user='root', password='', database='gamemana')
    cursor = conn.cursor()
    cursor.execute('select * from gm_game_user where id<200000')
    values = cursor.fetchall()
    cursor.close()
    conn.close()

t = threading.Thread(target=select, name='selectThread1')
k = threading.Thread(target=select2, name='selectThread2')
t.start()
k.start()
t.join()
k.join()
