import socket
import fib
from multiprocessing import Process

def fib_server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    while True:
        print("Waiting for connection")
        client, addr = sock.accept()
        print("Connection", addr)
        Process(target=fib_handler, args=(client,), daemon=True).start()


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break

        n = int(req)
        result = fib.fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print("Closed")

def main():
    fib_server(("", 25000))


if __name__ == '__main__':
    main()