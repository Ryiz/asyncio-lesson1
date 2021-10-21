import asyncio
from contextvars import ContextVar

#MyCounter = ContextVar('counter', default=0



async def count(counter):
    print(f'Колисество записей в списке: {len(counter)}')

    while True:
        await asyncio.sleep(1/1000)
        counter.append(1)

async def print_every_one_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- 1 секунда прошла. '
              f'Количество записей в списке: {len(counter)}')

async def print_every_five_sec():
    while True:
        await asyncio.sleep(5)
        print('----- 5 секунда прошло. ')

async def print_every_ten_sec():
    while True:
        await asyncio.sleep(10)
        print(f'-------- 10 секунда прошло. ')

async def main():
    counter = list()

    task = [
        count(counter),
        print_every_one_sec(counter),
        print_every_five_sec(),
        print_every_ten_sec()
    ]

    await asyncio.gather(*task)





asyncio.run(main())
