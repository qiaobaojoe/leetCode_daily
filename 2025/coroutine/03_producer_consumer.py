import asyncio
import random


async def producer(queue: asyncio.Queue, producer_id: int):
    for i in range(5):
        # 生产数据
        item = f"Producer {producer_id} - Item {i}"
        await queue.put(item)
        print(f"生产者 {producer_id} 生产: {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))


async def consumer(queue: asyncio.Queue, consumer_id: int):
    while True:
        try:
            # 消费数据
            item = await queue.get()
            print(f"消费者 {consumer_id} 消费: {item}")
            await asyncio.sleep(random.uniform(0.1, 0.3))
            queue.task_done()
        except asyncio.CancelledError:
            break


async def main():
    # 创建队列
    queue = asyncio.Queue(maxsize=5)

    # 创建生产者和消费者
    producers = [producer(queue, i) for i in range(2)]
    consumers = [consumer(queue, i) for i in range(3)]

    # 启动所有生产者
    await asyncio.gather(*producers)

    # 等待队列清空
    await queue.join()

    # 取消所有消费者
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    asyncio.run(main())
