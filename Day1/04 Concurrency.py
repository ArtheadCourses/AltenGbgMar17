from multiprocessing import Process, Queue

def worker(q):
    q.put(['hi', 43, None])

def main():
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()


if __name__ == '__main__':
    main()