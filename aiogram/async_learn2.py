import asyncio, time


async def my_function_sec(sec: int):
    await asyncio.sleep(sec)
    print(f'Пройшлo {sec} сек.')


async def main():
    task_1 = asyncio.create_task(my_function_sec(1))
    task_2 = asyncio.create_task(my_function_sec(5))

    await task_1
    await task_2


if __name__ == '__main__':
    for i in range(10):
        asyncio.run(main())
