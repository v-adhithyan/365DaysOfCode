import logging
import threading
import time
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info(f"Thread {name} starting to update..")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info(f"Thread {name} finishing update..")


def thread_func(name):
    logging.info(f"Thread {name} starting..")
    time.sleep(2)
    logging.info(f"Thread {name} exiting..")


def init_logging():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


def main1():
    threads = list()
    for i in range(3):
        logging.info(f"Main : create and start thread {i}")
        x = threading.Thread(target=thread_func, args=(i,))
        threads.append(x)
        x.start()

    for i, thread in enumerate(threads):
        logging.info(f"Main : before joining thread {i}")
        thread.join()
        logging.info(f"Main: thread {i} done.")


def main2():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_func, range(3))


def main3():
    db = FakeDatabase()
    logging.info(f"Test update. starting value is {db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(db.update, range(2))
    logging.info(f"Test update. ending value is {db.value}")


if __name__ == "__main__":
    init_logging()
    # main2()
    main3()
