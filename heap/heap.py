from typing import List, Optional


class MaxHeap:
    """
    大顶堆
    完全二叉树,用数组表示
    """

    def __init__(self, nums: List[int]):
        self.heap_list = nums
        self.heap_size = len(nums)

    def __init__(self):
        self.heap_list = []
        self.heap_size = 0

    def push(self, num: int):
        pass

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("空堆!!")

    def peek(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.heap_list[0]

    def size(self) -> int:
        return self.heap_size

    def is_empty(self) -> bool:
        return self.heap_size == 0


def main():
    max_heap = MaxHeap()
    print(max_heap.size())
    print(max_heap.is_empty())


if __name__ == "__main__":
    main()
