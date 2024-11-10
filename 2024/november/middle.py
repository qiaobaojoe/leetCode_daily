from math import sqrt
from typing import List


class MiddleSolution:
    def count_complete_day_pairs(self, hours: List[int]) -> int:
        hours_remaind = {}
        for hour in hours:
            hours_remaind[(hour % 24)] = hours_remaind.get((hour % 24), 0) + 1
        ans = self.pairs_help(hours_remaind.get(0, 0)) + self.pairs_help(
            hours_remaind.get(12, 0)
        )
        for i in range(1, 12):
            ans += self.pairs_help_two(
                hours_remaind.get(i, 0), hours_remaind.get(24 - i, 0)
            )
        return ans

    def pairs_help(self, k: int) -> int:
        if k < 2:
            return 0
        if k == 2:
            return 1

        return k * (k - 1) // 2

    def pairs_help_two(self, k: int, n: int) -> int:
        if k == 0 or n == 0:
            return 0
        return n * k

    def judge_square_sum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l < r:
            if l * l + r * r == c:
                return True
            if l * l + r * r < c:
                l += 1
            else:
                r -= 1
        return False

    def results_array(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        ans = [-1] * (n - k + 1)
        constant_range = []
        # 找到所有 >= k的连续区间
        start, end = -1, -1
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                if start == -1:
                    start = i
                end = i + 1
                if i == n - 2:
                    constant_range.append((start, end))
            else:
                if start != -1 and end - start + 1 >= k:
                    constant_range.append((start, end))
                start, end = -1, -1
        if len(constant_range) == 0:
            return ans
        for s, e in constant_range:
            for i in range(s, e - k + 2):
                ans[i] = nums[i + k - 1]
        return ans

    def single_non_duplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, n - 1
        while r > l:
            m = (r + l) // 2
            if m % 2 != 0:
                if m < n - 2:
                    m += 1
                else:
                    m -= 1

            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                if nums[m] == nums[m - 1]:
                    r = m - 2
                else:
                    return nums[m]
        return nums[l]


def main():
    solution = MiddleSolution()
    print(solution.single_non_duplicate([0, 1, 1]))


if __name__ == "__main__":
    main()
