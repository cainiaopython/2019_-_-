
import time


def count_running_time(func):
    '''
    count the fun running time
    :param func: 
    :return: 
    '''
    start = time.time()
    def wrap(*args):
        func(*args)
        cost_time=round(time.time()-start,1)
        print (f'Cots time:{cost_time}s')

    return wrap


@count_running_time
def show():
    print('Hello')
    time.sleep(3)

if __name__=='__main__':
    show()














