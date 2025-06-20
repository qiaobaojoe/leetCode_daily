def number_coroutine():
    result = 0
    while True:
        x = yield result  # 返回当前结果并等待下一个值
        if x is None:
            break
        result += x


# 使用示例
def demo_coroutine():
    # 创建协程对象
    nc = number_coroutine()
    # 启动协程
    next(nc)

    # 发送值并获取结果
    print(nc.send(1))  # 输出: 1
    print(nc.send(2))  # 输出: 3
    print(nc.send(3))  # 输出: 6

    try:
        nc.send(None)  # 终止协程
    except StopIteration:
        pass


if __name__ == "__main__":
    demo_coroutine()
