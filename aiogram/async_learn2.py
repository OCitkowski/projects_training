import asyncio, time


async def my_function_sec(sec: int):
    await asyncio.sleep(sec)
    print(f'Пройшлo {sec} сек.')


async def main():
    task_1 = asyncio.create_task(my_function_sec(2))
    task_2 = asyncio.create_task(my_function_sec(1))

    await task_1
    await task_2

async def main_cl():

    a1 = MyClassAsync(4)
    a2 = MyClassAsync(3)

    task1 = asyncio.create_task(a1.my_function_sec())
    task2 = asyncio.create_task(a2.my_function_sec())

    await asyncio.gather(task1, task2)

    # l_task = ()
    # for i in range(19):
    #     a = MyClassAsync(i)
    #     task = asyncio.create_task(a.my_function_sec())
    #     l_task.add(task)
    # t_task = *l_task
    await asyncio.gather(*[my_function_sec(i) for i in range(6, 1, -1)])

class MyClassAsync():

    def __init__(self, sec: int):
        self.sec = sec


    async def my_function_sec(self):
        await asyncio.sleep(self.sec)
        print(f'Минуло - {self.sec} сек.')

    # async def main(self):
    #     task = asyncio.create_task(self.my_function_sec())
    #     return await task


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.run(main_cl())