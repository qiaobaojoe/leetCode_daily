import asyncio
from typing import AsyncIterator


class AsyncResource:
    async def __aenter__(self):
        print("获取资源")
        await asyncio.sleep(1)  # 模拟资源获取
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("释放资源")
        await asyncio.sleep(0.5)  # 模拟资源释放

    async def process(self):
        print("使用资源处理数据")
        await asyncio.sleep(1)


async def main():
    async with AsyncResource() as resource:
        await resource.process()


if __name__ == "__main__":
    asyncio.run(main())
