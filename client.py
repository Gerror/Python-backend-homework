import argparse
import threading
import socket


def fetch_urls(domains):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect(("127.0.0.1", 15000))
    for domain in domains:
        url = f"https://{domain}/"
        connection.send(url.encode())
        resp = connection.recv(4096)
        print(f"{url}: {resp.decode()}")
    connection.close()

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str)
    parser.add_argument("-m", type=int)
    return vars(parser.parse_args())

def read_domains_from_file(filename):
    with open(filename, "r") as f:
        return f.read().split('\n')

def main():
    args = get_args()
    domains = read_domains_from_file(args.get('input'))

    domains_for_thread = len(domains) // args.get('m')
    threads = [
        threading.Thread(target=fetch_urls,
                         args=(domains[i * domains_for_thread:(i + 1) * domains_for_thread],))
        for i in range(args.get('m'))
    ]

    for th in threads:
        th.start()
    for th in threads:
        th.join()


if __name__ == '__main__':
    main()