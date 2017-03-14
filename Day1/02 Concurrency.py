from multiprocessing import Process


def worker(name):
    print(name, "Work work")

def main():
    t1 = Process(target=worker, args=("John",))
    t1.start()
    t2 = Process(target=worker, args=("Anna",))
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()