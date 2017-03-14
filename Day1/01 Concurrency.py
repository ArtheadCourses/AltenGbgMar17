from threading import Thread, Lock


def main():
    print_lock = Lock()

    def worker():
        with print_lock:
            print("Work work")

    t1 = Thread(target=worker)
    t1.start()
    t2 = Thread(target=worker)
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()