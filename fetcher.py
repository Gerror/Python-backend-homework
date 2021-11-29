import argparse
import asyncio
import aiohttp
from time import time


async def fetch_urls(urls, session):
    for url in urls:
        print("Current url:", url)
        async with session.get(url) as resp:
            data = await resp.text()
            with open(f'data/{time()}', 'w') as f:
                f.write(data)

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str)
    parser.add_argument("-m", type=int)
    return vars(parser.parse_args())

def read_urls_from_file(filename):
    with open(filename, "r") as f:
        return f.read().split('\n')

async def main():
    args = get_args()
    urls = read_urls_from_file(args.get('input'))

    urls_for_thread = len(urls) // args.get('m')
    start_time = time()
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch_urls(urls[i * urls_for_thread:(i + 1) * urls_for_thread], session))
            for i in range(args.get('m'))
        ]
        await asyncio.gather(*tasks)
    print("Time:", time() - start_time)

if __name__ == '__main__':
    asyncio.run(main())