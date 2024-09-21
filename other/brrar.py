import threading
import time
from concurrent.futures import ThreadPoolExecutor
import random
from threading import Barrier

thread_pool = ThreadPoolExecutor(max_workers=10)


def task(args):
    print(f'hello world  {args}')


thread_pool.submit(task, (1, 3, 4))

barrier = Barrier(5, timeout=10)


class CountDownLatch(object):
    def __init__(self, count=1):
        self.count = count
        self.lock = threading.Condition()

    def count_down(self):
        self.lock.acquire()
        self.count -= 1
        if self.count <= 0:
            self.lock.notifyAll()
        self.lock.release()

    def _await(self):
        self.lock.acquire()
        while self.count > 0:
            self.lock.wait()
        self.lock.release()


count_down_latch = CountDownLatch(5)


class Task(threading.Thread):

    def run(self):
        time.sleep(random.random())
        print('--------------')
        count_down_latch.count_down()


if __name__ == '__main__':
    for i in range(4):
        t = Task()
        t.start()
    count_down_latch._await()
    print('Down')
