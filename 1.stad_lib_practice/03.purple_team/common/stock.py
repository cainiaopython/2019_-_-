from threading import  Thread
from datetime import datetime
from config import *
import time
import tushare as ts

class Stock():
    '''
    获取股票的实时信息
    '''
    def __init__(self):
        self._terminal=True
        self._price=0

    @property
    def stock_price(self):
        return self._price

    def query_stock_real_price(self,stock_num):
        df = ts.get_realtime_quotes(stock_num)
        df=df[['price','time']]
        price=df['price'].values[0]
        return  float(price)

    def get_kline_data(self, ktype='ma5'):
        today=datetime.now().strftime('%Y-%m-%d')
        df = ts.get_hist_data(self.stock_num, start='2018-08-08', end=today)
        return (df[[ktype]])



if __name__=='__main__':
    stock=Stock()
    p=stock.query_stock_real_price('000001')
    print ('p:{}'.format(p))



































