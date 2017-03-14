import socket
import time
from threading import Thread

n  = 0
def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, 'reqs/sec')
        n = 0

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost',25000))
    Thread(target=monitor).start()
    global n
    while True:
        sock.send(b'1')
        resp = sock.recv(100)
        n += 1



if __name__ == '__main__':
    main()