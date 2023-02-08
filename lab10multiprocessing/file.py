#multiprocessing :DDDDDDDD

import numpy as np

import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def fibon(n):
    if n < 2:
        return n
    else:
        return (fibon(n-1)+fibon(n-2))

def fibon_job(n):
    val = fibon(n)

    return n, val
def zaWarudo():
    print("ZA WARUDO")
    return "Muda"

start = time.time()
if __name__ == '__main__':
    with ProcessPoolExecutor(3) as ex:
        futures = [ex.submit(fibon_job,n) for n in range(30)]
        for f in as_completed(futures):
            print(f.result())
stop = time.time()
print(stop-start)
#if __name__ == '__main__':
#    with ProcessPoolExecutor(3) as ex:
#        futures = [ex.submit(zaWarudo) for _ in range(10)]
#        for f in futures:
#            print(f.result())


#start = time.time()
#for n in range(10):
#    print(fibon(n))
#stop = time.time()
#print(f'{stop - start= }')