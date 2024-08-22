import asyncio
import time


async def start_strongman(name, power):
    factor = 10
    print(f"Силач {name} начал соревнования")
    for up in range(1,6):
        await asyncio.sleep(factor/power)
        print(f"Силач {name} поднял {up}")
    print(f"Силач {name} закончил соревнования")


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman("Dan", 2))
    task_2 = asyncio.create_task(start_strongman("Vinchenzo", 4))
    task_3 = asyncio.create_task(start_strongman("Ron", 3))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())


