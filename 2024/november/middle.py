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
        if c == 0:
            return True
        for i in range(0, c):
            if i * i > c:
                return False
            b = c - i * i
            if sqrt(b) == int(sqrt(b)):
                return True
        return False


def main():
    solution = MiddleSolution()
    print(solution.judge_square_sum(0))


if __name__ == "__main__":
    main()
