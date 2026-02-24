from multiprocessing import Process
import time


def task(name, seconds):
    print(f"{name} starting...")
    time.sleep(seconds)
    print(f"{name} finished after {seconds}s")


if __name__ == "__main__":
    p1 = Process(target=task, args=("Process-A", 2))
    p2 = Process(target=task, args=("Process-B", 3))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes done!")