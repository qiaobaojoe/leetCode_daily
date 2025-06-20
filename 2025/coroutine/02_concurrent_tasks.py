import asyncio
import time

async def async_task(task_id: int, delay: float):
    print(f"任务 {task_id} 开始执行")
    await asyncio.sleep(delay)  # 模拟不同耗时的IO操作
    print(f"任务 {task_id} 执行完成")
    return f"任务 {task_id} 的结果"

async def main():
    # 创建多个任务
    tasks = [
        async_task(1, 2),
        async_task(2, 1),
        async_task(3, 3)
    ]
    
    # 并发执行所有任务
    start_time = time.time()
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    
    print(f"\n所有任务完成，耗时: {end_time - start_time:.2f}秒")
    print(f"结果: {results}")

if __name__ == "__main__":
    asyncio.run(main())