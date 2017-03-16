import asyncio


async def countdown(number, n):
    while n > 0:
        print("T-minus", n, '({})'.format(number))
        await asyncio.sleep(1)
        n -= 1

def main():
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(countdown("A", 5)),
        asyncio.ensure_future(countdown("B", 4))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()



if __name__ == '__main__':
    main()