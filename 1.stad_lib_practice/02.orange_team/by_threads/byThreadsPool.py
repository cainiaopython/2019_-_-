from concurrent.futures import ThreadPoolExecutor
from spider.spider import Spider
from pprint import pprint
from common.costTime import count_running_time

MAX_THREADS=5
crawl=Spider()


@count_running_time
def run_threads_pool(words):
    executor=ThreadPoolExecutor(MAX_THREADS)
    tasks = [executor.submit(crawl.crawl_each, (w)) for w in words]

    out=[t.result() for t in tasks ]
    pprint(out)

if __name__=='__main__':
    words = ['china', 'english', 'temperaments'] * 100
    run_threads_pool(words)