import time
from multiprocessing import Process, Queue


def eat(q):
    for i in range(5):
        dinner = q.get()
        print(f" Eating {dinner}")
        time.sleep(1)


def make_dinner(q):
    for i in range(5):
        print(f"Making dinner... {i + 1}")
        q.put(f"Dinner {i + 1}")
        time.sleep(1)


if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=eat, args=(q,))
    p2 = Process(target=make_dinner, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")
