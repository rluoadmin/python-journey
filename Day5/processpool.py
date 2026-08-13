import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def work(n):
    print(f"Working on {n} in process {os.getpid()}")
    time.sleep(2)
    return n * n


if __name__ == "__main__":
    print("Starting.")
    executor = ProcessPoolExecutor(3)

    futures = []
    for i in range(10):
        future = executor.submit(work, i)
        future.add_done_callback(
            lambda f: print(f"Task completed with result: {f.result()}")
        )
        futures.append(future)

    # futures = [executor.submit(work, i) for i in range(10)]

    for future in as_completed(futures):
        result = future.result()
        print(f"Result: {result}")

    executor.shutdown(wait=True)

    print("Done!")
