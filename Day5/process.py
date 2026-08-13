import os
import time
from multiprocessing import Process


def eat():
    for i in range(5):
        print(f"Eating... {i + 1} and pid: {os.getpid()}")
        time.sleep(1)


def drink():
    for i in range(10):
        print(f"Drinking... {i + 1} and pid: {os.getpid()}")
        time.sleep(1)


def daemon():
    print(f"Daemon process started with pid: {os.getpid()}")
    while True:
        print("Daemon is running...")
        time.sleep(1)


if __name__ == "__main__":
    d1 = Process(target=daemon, daemon=True)
    p1 = Process(target=eat)
    p2 = Process(target=drink)

    d1.start()
    p1.start()
    p2.start()
    for i in range(5):
        print(f"Main process is running... {i + 1} and pid: {os.getpid()}")
        time.sleep(1)

    print("Done!")
