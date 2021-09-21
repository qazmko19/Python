import asyncio
import os


async def read_future(future):
    while True:
        try:
            file = open("dz2.txt", 'r')
            file_read = file.read()
            if file_read == "Wow!":
                file.close()
                future.set_result('This file is includes "Wow!"')
                break
            else:
                print('This file isn`t include "Wow!"')
                await asyncio.sleep(5)
        except FileNotFoundError:
            print("File not available")
            await asyncio.sleep(5)


async def wait_read_future(future):
    result = await future
    print(result)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dz2.txt")
    os.remove(path)


event_loop = asyncio.get_event_loop()
fut = asyncio.Future()

tasks_list = [
    event_loop.create_task(read_future(fut)),
    event_loop.create_task(wait_read_future(fut))
]
tasks = asyncio.wait(tasks_list)
event_loop.run_until_complete(tasks)

event_loop.close()
