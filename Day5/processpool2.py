import os
import time
from concurrent.futures import ThreadPoolExecutor
from threading import get_native_id

# def work(n):
#     print(f"Working on {n} in thread {os.getpid()}")
#     time.sleep(2)
#     return n * n


def workThread(n):
    print(f"Working on {n} in thread {get_native_id()}")
    time.sleep(2)
    return n * n


if __name__ == "__main__":
    # with ProcessPoolExecutor(3) as executor:
    #     results = executor.map(work, range(10))
    #     print("Results:", list(results))

    with ThreadPoolExecutor(3) as executor:
        results = executor.map(workThread, range(10))
        print("Results:", list(results))
