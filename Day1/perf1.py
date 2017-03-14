import socket
import time

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost',25000))

    while True:
        start = time.time()
        sock.send(b'30')
        resp = sock.recv(100)
        end = time.time()
        print(end - start, 's')


if __name__ == '__main__':
    main()