import asyncio


async def hello_world():
    print("开始执行协程")
    await asyncio.sleep(1)  # 模拟IO操作
    print("协程执行完成")
    return "Hello, World!"


async def main():
    print("主协程开始")
    result = await hello_world()
    print(f"获得结果: {result}")
    print("主协程结束")


# 运行协程
if __name__ == "__main__":
    asyncio.run(main())
