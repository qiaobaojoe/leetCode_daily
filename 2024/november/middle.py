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
        for i in range(n - k + 1):
            cur = nums[i : i + k]
            is_constant = True
            for j in range(1, k):
                if cur[j] != cur[j - 1] + 1:
                    is_constant = False
                    break

            if is_constant:
                ans[i] = cur[k - 1]
        return ans


def main():
    solution = MiddleSolution()
    print(solution.results_array([1, 2, 3, 4, 3, 2, 5], 3))


if __name__ == "__main__":
    main()
