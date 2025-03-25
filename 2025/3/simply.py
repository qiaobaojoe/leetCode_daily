from typing import List
import asyncio


class Solution:
    def count_prefixes(self, words: List[str], s: str) -> int:
        ans = 0
        prefix_word = []
        for i in range(len(s)):
            prefix_word.append(s[: i + 1])
        print(prefix_word)
        for word in words:
            if len(word) > len(s):
                continue
            if word == prefix_word[len(word) - 1]:
                ans += 1
        return ans


def coroutine_decorator(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # 预激活协程
        return gen
    return wrapper

@coroutine_decorator
def receiver():
    while True:
        value = yield
        print(f'接收到值: {value}')



async def async_task(name, delay):
    print(f'{name} 开始')
    await asyncio.sleep(delay)
    print(f'{name} 完成')
    return f'{name} 的结果'

async def main():
    # 并发执行多个协程
    tasks = [
        async_task('任务1', 1),
        async_task('任务2', 2),
        async_task('任务3', 3)
    ]
    results = await asyncio.gather(*tasks)
    print(results)

# 运行异步程序
asyncio.run(main())

# def main():
#     # 创建协程
#     r = receiver()
#     # 发送值给协程
#     r.send('Hello')

#     r.send(42)


# if __name__ == "__main__":
#     main()
