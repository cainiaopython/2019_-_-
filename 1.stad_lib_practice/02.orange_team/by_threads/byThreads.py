import threading
from spider.spider import Spider
from common.costTime import count_running_time


@count_running_time
def run_threading(words):
    crawl = Spider()
    threads=[threading.Thread(target=crawl.crawl_each,args=(w,)) for w in words]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__=='__main__':
    words = ['china', 'english', 'temperaments'] * 100
    run_threading(words)

