import queue
import threading
from spider.spider import Spider
from common.costTime import count_running_time


crawl=Spider()
MAX_THREAD=5

def handle_thread(queue):
    while not queue.empty():
        data=queue.get()
        crawl.crawl_each(data)

@count_running_time
def run_thread_as_queue(words):
    threads=[]
    q=queue.Queue()

    for w in words:
        q.put(w)

    threads=[threading.Thread(target=handle_thread,args=(q,))for _ in range(MAX_THREAD)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__=='__main__':
    words = ['china', 'english', 'temperaments'] * 100
    run_thread_as_queue(words)
