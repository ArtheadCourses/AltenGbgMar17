from multiprocessing import Process, Pipe

def worker(conn):
    conn.send(['hi', 43, None])
    conn.close()

def main():
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.close()
    p.join()


if __name__ == '__main__':
    main()