from typing import List, Optional


class MaxHeap:
    """
    大顶堆
    完全二叉树,用数组表示
    """

    def __init__(self, nums: List[int]):
        self.heap_list = nums

    def __init__(self):
        self.heap_list = []

    def push(self, num: int):
        self.heap_list.append(num)
        self._sift_up(self.size() - 1)

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("空堆!!")
        self._swap(0, self.size() - 1)
        val = self.heap_list.pop()
        self._sift_down(0)
        return val

    def peek(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.heap_list[0]

    def size(self) -> int:
        return len(self.heap_list)

    def is_empty(self) -> bool:
        return self.size() == 0

    def _left(self, i: int) -> int:
        """
        左子节点位置
        """
        return 2 * i + 1

    def _right(self, i: int) -> int:
        """
        右子节点位置
        """
        return 2 * i + 2

    def _parent(self, i: int) -> int:
        """
        父节点位置
        """
        return (i - 1) // 2

    def _sift_up(self, i: int):
        """
        当前元素向堆顶化
        和他的父元素比较,比他大就交换元素
        """
        if i == 0:
            return
        parent_i = self._parent(i)

        while i > 0 and self.heap_list[parent_i] < self.heap_list[i]:
            self._swap(i, parent_i)
            i = parent_i
            parent_i = self._parent(i)

    def _sift_down(self, i: int):
        left_i = self._left(i)
        right_i = self._right(i)
        cur = i

        while left_i < self.size():
            l_val = self.heap_list[left_i]
            cur_val = self.heap_list[cur]
            if right_i >= self.size():
                if l_val > cur_val:
                    self._swap(left_i, cur)
                break
            r_val = self.heap_list[right_i]

            if l_val > r_val:
                if l_val > cur_val:
                    self._swap(left_i, cur)
                    cur = left_i
                    left_i = self._left(cur)
                    right_i = self._right(cur)
                else:
                    break
            else:
                if r_val > cur_val:
                    self._swap(right_i, cur)
                    cur = right_i
                    left_i = self._left(cur)
                    right_i = self._right(cur)
                else:
                    break

    def _swap(self, i: int, parent_i: int):
        cur = self.heap_list[i]
        self.heap_list[i] = self.heap_list[parent_i]
        self.heap_list[parent_i] = cur


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        max_heap = MaxHeap()
        for num in nums:
            max_heap.push(num)
        for _ in range(k - 1):
            max_heap.pop()
        return max_heap.pop()


def main():
    max_heap = MaxHeap()
    print(max_heap.size())
    print(max_heap.is_empty())
    max_heap.push(1)
    max_heap.push(4)
    max_heap.push(3)
    max_heap.push(6)
    max_heap.push(2)
    max_heap.push(6)
    max_heap.push(7)
    max_heap.push(5)
    max_heap.push(2)
    max_heap.push(8)
    max_heap.push(6)
    max_heap.push(9)
    print(max_heap.size())
    print(max_heap.is_empty())
    print(max_heap.heap_list)
    max_heap.pop()
    print(max_heap.heap_list)
    max_heap.pop()
    print(max_heap.heap_list)


if __name__ == "__main__":
    main()
