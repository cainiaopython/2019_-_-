import asyncio
from spider.spider import Spider
from common.costTime import count_running_time
from pprint import pprint
from spider.async_spider import *


@count_running_time
def run_asyncio(words):
    run_as_asyncio(words)


if __name__=='__main__':
    words = ['china', 'english', 'temperaments'] * 100
    run_asyncio(words)

