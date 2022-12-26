import asyncio


class Limiter():

    """

    The purpose of this class is to limit the invocation of increment()
    based on a evaluation of 'some_condition' wrt. the class's internal state.

    """

    def __init__(self) -> None:
        self.counter, self.limit = 0, 5

        self.loop = asyncio.get_event_loop()
        self.__schedule_tasks()

    def __schedule_tasks(self) -> None:
        """ Minimal selection of tasks for this demonstation. """

        self.loop.create_task(self.reset_counter())
        self.loop.create_task(self.display())

    def _increment(self) -> None:
        """ Increment counter variable. """

        print('Incrementing counter')
        self.counter += 1

    async def reset_counter(self) -> None:
        """ Periodically (10s) reset the counter value. """

        while True:
            print('Resetting Counter')
            self.counter = 0
            await asyncio.sleep(10)

    async def display(self) -> None:
        """ Periodically (1s) display the counter value. """

        while True:
            print(self.counter)
            await asyncio.sleep(1)

    async def increment(self) -> bool:
        """ Provided that some_condition is met, call increment(). """

        some_condition = (self.counter < 5)

        if (some_condition):
            self._increment()
            return True

        print('some_condition not met - Not able to call increment().')
        return False

class Caller():
    """

    An object interfacing with the limiter.

    Periodicalyl call limiter.increment()
    Calls to increment() should be restricted by the limiter based
    on the evaluation of 'some_condition' wrt the limiters internal state.

    """

    def __init__(self) -> None:
        self.limiter = Limiter()

        self.loop = asyncio.get_event_loop()
        self.schedule_tasks()

    def schedule_tasks(self) -> None:
        """ Minimal selection of tasks for this demonstation. """

        self.loop.create_task(self.make_call())

    async def make_call(self) -> None:
        """ Periodically (1s) call increment. """

        while True:
            await self.limiter.increment()
            await asyncio.sleep(1)


def main():
    try:
        loop = asyncio.get_event_loop()
        caller = Caller()
        loop.run_forever()

    except KeyboardInterrupt:
        print('Stopping event loop')
        loop.stop()


if __name__ == "__main__":
    main()
