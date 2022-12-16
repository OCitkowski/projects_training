import asyncio, time


async def my_function_3sec():
    await asyncio.sleep(3)
    print('Пройшлo 3 сек.')


async def my_function_1sec():
    await asyncio.sleep(1)
    print('Пройшлo 1 сек.')


async def main():
    task_1 = asyncio.create_task(my_function_3sec())
    task_2 = asyncio.create_task(my_function_1sec())

    await task_1
    await task_2


if __name__ == '__main__':
    for i in range(10):
        print(i * 3)
        asyncio.run(main())

