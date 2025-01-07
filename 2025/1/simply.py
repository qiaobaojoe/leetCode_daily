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
        return max(ans, top - start + 1)

    def count_key_changes(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            diff = ord(s[i + 1]) - ord(s[i])
            if diff == 0 or diff == 32 or diff == -32:
                continue
            ans += 1
        return ans


def main():
    solution = Solution()
    print(solution.count_key_changes("aAbBcC"))


if __name__ == "__main__":
    main()
