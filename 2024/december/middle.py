from functools import cache
from heapq import heapify, heappop, heappush
from typing import List


class MiddleSolution:

    @cache
    def knight_probability(self, n: int, k: int, row: int, column: int) -> float:

        if row < 0 or row >= n or column < 0 or column >= n:
            return 0
        if k == 0:
            return 1
        probablility = 0

        # 每一步有8个方向可以走
        # 上2
        probablility += self.knight_probability(n, k - 1, row - 2, column - 1) / 8
        probablility += self.knight_probability(n, k - 1, row - 2, column + 1) / 8
        # 上1
        probablility += self.knight_probability(n, k - 1, row - 1, column - 2) / 8
        probablility += self.knight_probability(n, k - 1, row - 1, column + 2) / 8
        # 下2
        probablility += self.knight_probability(n, k - 1, row + 2, column - 1) / 8
        probablility += self.knight_probability(n, k - 1, row + 2, column + 1) / 8
        # 下1
        probablility += self.knight_probability(n, k - 1, row + 1, column - 2) / 8
        probablility += self.knight_probability(n, k - 1, row + 1, column + 2) / 8

        return probablility

    def max_spending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        q = [(values[i][-1], i, n - 1) for i in range(m)]
        heapify(q)
        ans = 0
        for turn in range(1, m * n + 1):
            val, i, j = heappop(q)
            ans += val * turn
            if j > 0:
                heappush(q, (values[i][j - 1], i, j - 1))
        return ans

    def get_final_state(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_i = 0
            for i, n in enumerate(nums):
                if n < nums[min_i]:
                    min_i = i
            nums[min_i] *= multiplier
        return nums

    def min_set_size(self, arr: List[int]) -> int:
        num_count = {}
        for n in arr:
            if n not in num_count:
                num_count[n] = 0
            num_count[n] += 1
        count_list = list(num_count.values())
        count_list.sort(reverse=True)
        half = len(arr) // 2
        count = 0
        for i, c in enumerate(count_list):
            count += c
            if count >= half:
                return i + 1
        return -1


def main():
    solution = MiddleSolution()
    print(solution.min_set_size([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))


if __name__ == "__main__":
    main()
