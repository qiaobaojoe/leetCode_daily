from typing import List


class Solution:
    def max_consecutive(self, bottom: int, top: int, special: List[int]) -> int:
        if bottom == top:
            return 0
        floor_size = top - bottom + 1
        if len(special) == floor_size:
            return 0

        ans = 0
        special.sort()
        start = bottom
        for s in special:
            if s > start:
                ans = max(ans, s - start)
            start = s + 1
        return max(ans, top - start +1)


def main():
    solution = Solution()
    print(solution.max_consecutive(2, 9, [4, 6]))


if __name__ == "__main__":
    main()
