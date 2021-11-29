import argparse
import threading
import socket
import queue
import requests
import json
from collections import Counter

client_socks = queue.Queue()
worker_stats = 0

def worker_response(url, k):
    try:
        result = requests.get(url)
        result = result.text.replace("\n", " ")
        result = result.replace("\t", " ")
        result = filter(None, result.split(" "))
        most_common = Counter(result).most_common(k)
        return json.dumps(dict(most_common))
    except ConnectionError as error:
        return error

def worker(k):
    global worker_stats
    while True:
        if not client_socks.empty():
            client_sock = client_socks.get()
            while True:
                data = client_sock.recv(4096)

                if not data:
                    break
                else:
                    client_sock.send(worker_response(data.decode(), k).encode())
                    worker_stats += 1
                    print(f"All requests: {worker_stats}")
            client_sock.close()

def master():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('127.0.0.1', 15000))
    server_sock.listen()
    while True:
        client_sock, addr = server_sock.accept()
        client_socks.put(client_sock)

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-w", type=int)
    parser.add_argument("-k", type=int)
    return vars(parser.parse_args())

def main():
    args = get_args()

    master_th = threading.Thread(target=master, daemon=True)
    worker_ths = [
        threading.Thread(target=worker, args=(args.get('k'),), daemon=True) for _ in range(args.get('w'))
    ]

    for th in worker_ths:
        th.start()
    master_th.start()

    try:
        for th in worker_ths:
            th.join()
        master_th.join()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()