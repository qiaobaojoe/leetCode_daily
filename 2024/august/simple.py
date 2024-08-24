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

    def find_permutation_difference(self, s: str, t: str) -> int:
        t_map = {}
        for i,t_char in enumerate(t):
            t_map[t_char] = i

        ans = 0
        for i,s_char in enumerate(s) :
            ans += abs(i-t_map[s_char])  
        return ans


def main():
    solution = Solution()
    print(solution.find_permutation_difference("abc", "bac"))


if __name__ == "__main__":
    main()
