#!/usr/bin/env python3

# TODO Daemon \ Notifications \ Flask WebUI Reportings

from sqlite3 import connect, OperationalError
from sys import exit
from datetime import datetime
from urllib.request import urlopen, URLError


def db_setup(db = "db.sqlite"):
  try:
    conn = connect(db)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS temnet (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, DATA TEXT NOT NULL, STATUS TEXT NOT NULL, URL TEXT NOT NULL, STATUS_CODE TEXT NOT NULL, IP TEXT NOT NULL)''')
    conn.close()
  except(OperationalError):
    print("Falha na conexao com o banco!")
    exit(1)


def db_insert(data,status,url,code,ip,db = "db.sqlite"):
  try:
    conn = connect(db)
    cur = conn.cursor()
    cur.execute('INSERT INTO temnet (DATA,STATUS,URL,STATUS_CODE,IP) VALUES(?,?,?,?,?)',(data,status,url,code,ip))
    conn.commit()
    conn.close()
  except(OperationalError):
    print("Falha na conexao com o banco!")
    exit(1)  


def main(url="https://google.com.br",api="https://api.ipify.org"):
  db_setup()
  data = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
  try:
    with urlopen(url) as response:
      response_content, response_status = response.read(), response.getcode()
    with urlopen(api) as ip:
      ip_content = ip.read().decode("utf-8")
    print("Conexao OK! IP: {0}".format(ip_content))
    db_insert(data,"OK",url,response_status,ip_content)
  except(URLError):
    print("Conexao fora!")
    db_insert(data,"FALHA",url,"0","0.0.0.0")


if __name__ == "__main__":
  main()
