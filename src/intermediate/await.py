from collections.abc import Awaitable
from asyncio import Queue


def run_async(func: Awaitable[int]):
    ...


queue: Queue[int] = Queue()
queue2: Queue[str] = Queue()


async def async_function() -> int:
    return await queue.get()


async def async_function2() -> str:
    return await queue2.get()


run_async(async_function())
run_async(1)
run_async(async_function2())