import multiprocessing
import time
def put(queue):
    for i in range(5):
        if queue.full():
            print('已经满了')
            break
        else:
            time.sleep(0.2)
            queue.put(i)


def get(queue):
    while True:
        if queue.empty():
            print('已经为空')
            break
        num = queue.get()
        print(num)


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    queue = multiprocessing.Manager().Queue(3)
    result = pool.apply_async(put, (queue,))
    result.wait()
    pool.apply_async(get, (queue,))
    pool.close()
    pool.join()
