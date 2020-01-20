import gevent
import gevent.monkey
# if you use gevent ,must import before monkey
gevent.monkey.patch_all()


from spider.spider import Spider
from common.costTime import count_running_time

@count_running_time
def run_gevent(words):
    crawl = Spider()
    events=[gevent.spawn(crawl.crawl_each,w) for w in words ]
    results=gevent.joinall(events)
    for result in results:
        print (result.get())

if __name__=='__main__':
    words = ['china', 'english', 'temperaments'] * 100
    run_gevent(words)
