from common.server import Server
from pprint import pprint
from config.config import *
from common.mail import Mail
from common.stock import Stock
from threading import  Thread
from datetime import datetime
import queue
import os
import yaml
import time

def send_mail(title):
    try:
        server=Server(SMTP_SERVER,PASSWORD,FROM_ADDR)
        if server.connet():
            mail=Mail(server,TO_ADDRS)
            mail.mail_title=title
            mail.mail_content='股票提醒消息来了'
            mail.send_mail()
        server.close()
        print ('mail send out!')
    except Exception as e:
        print (e)
        print ('mail send failed!')


def read_yaml_data(yaml_file):
    yaml.warnings({'YAMLLoadWarning': False})

    file_data=None
    with open(yaml_file, 'r', encoding="utf-8") as file:
        file_data = file.read()

    data = yaml.load(file_data)
    return data


def verify_stock(stock,cur_price):

    stock_num = stock.get('num')

    high_price = float(stock.get('high'))
    low_price = float(stock.get('low'))

    print('stock:{},cur_price:{},high:{},low:{}'.format(stock_num,
                                         cur_price,
                                         high_price,
                                         low_price
                                         ))

    if cur_price > high_price or cur_price < low_price:
        title = '股票{}:当前价格{},预警最高:{},预警最低:{}'.format(stock_num,
                                                 cur_price,
                                                 high_price,
                                                 low_price)
        print(title)
        send_mail(title)

if __name__=='__main__':

    stock_num='000001' #平安银行
    stock=Stock()

    dir_path = os.path.abspath(os.path.dirname(__file__))
    yaml_path = os.path.join(dir_path, 'config/setting.yaml')

    while True:
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print (now_time)

        setting = read_yaml_data(yaml_path)
        monitor_flag=setting.get('monitor')

        if monitor_flag==0:
            print ('stop monitor')

        elif monitor_flag==-1:
            print ('exit!')
            break
        else:
            print ('Start Monitoring...')

            cur_price=stock.query_stock_real_price(stock_num)

            stocks = setting.get('stocks')
            stock_info= [s for s in stocks if s.get('num')==stock_num][0]
            verify_stock(stock_info,cur_price)

        time.sleep(60)

    print ('End!')

