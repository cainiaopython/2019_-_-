from by_asyncio import byAsyncio
from by_gevent import byGevent
from by_threads.byThreads import run_threading
from by_threads.byThreadsPool import run_threads_pool
from by_threads.byThreadsWithQueue import run_thread_as_queue


words = ['china', 'english', 'temperaments'] * 100
# byGevent.run_gevent(words)
# byAsyncio.run_as_asyncio(words)

# run_threading(words)

# run_threads_pool(words)

run_thread_as_queue(words)