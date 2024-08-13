from typing import List


class Solution:
    def is_array_special(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i, n in enumerate(nums[0 : len(nums) - 1]):
            remaind = (n + nums[i + 1]) % 2
            if remaind == 0:
                return False

        return True


def main():
    solution = Solution()
    print(solution.is_array_special([4, 3, 1, 6]))


if __name__ == "__main__":
    main()
