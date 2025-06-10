from functools import cache
from typing import List


class DpQuestion:

    def rob(self, nums: List[int]) -> int:
        # rob(n+1) = rob(n)(0) + rob(n-1)(1)
        n = len(nums)
        if n < 2:
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
        f = [0] * (n + 1)
        # 初始状态复制 第一家偷了，第二家没有偷
        f[0] = 0
        f[1] = nums[1]

        for i in range(2, n):
            f[i] = max(nums[i] + f[i - 2], f[i - 1])
        return f[n - 1]

    def rob_test(self):
        print(self.rob([2, 1, 1, 2]))

    def delete_and_earn(self, nums: List[int]) -> int:
        # 强  转化成rob，太强了
        val_sum = [0] * (max(nums) + 1)
        for num in nums:
            val_sum[num] += num
        return self.rob(val_sum)

    def delete_and_earn_test(self):
        print(self.delete_and_earn([3, 4, 2]))

    def unique_paths(self, m: int, n: int) -> int:
        # 很直接的dp思路 f[m][n] = f[m-1][n] + f[m][n-1]
        dp = [[0] * n for _ in range(m)]
        for y in range(1, m):
            dp[y][0] = 1
        for x in range(1, n):
            dp[0][x] = 1
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[m - 1][n - 1]

    def unique_paths_test(self):
        print(self.unique_paths(3, 7))

    def min_falling_path_sum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(matrix[0]):
            dp[0][i] = x
        for i in range(1, n):
            for j in range(0, n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == n - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = matrix[i][j] + min(
                        dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j - 1]
                    )
        return min(dp[n - 1])

    def min_falling_path_sum_test(self):
        print(self.min_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))

    def maximal_square(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1:
            if matrix[0][0] == "1":
                return 1
            else:
                return 0
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        for x in range(n):
            if matrix[0][x] == "1":
                dp[0][x] = 1
                max_side = 1
        for y in range(1, m):
            if matrix[y][0] == "1":
                dp[y][0] = 1
                max_side = 1
        for y in range(1, m):
            for x in range(1, n):
                if matrix[y][x] == "1":
                    dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1]) + 1
                    max_side = max(max_side, dp[y][x])
        return max_side * max_side

    def maximal_square_test(self):
        print(
            self.maximal_square(
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            )
        )

    # 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
    def longest_palindrome_subseq(self, s: str) -> int:
        # dp没有思路，先上最暴力的解法，在面试的时候也是如此，如果没有刷过题目，找不好状态方程，直接给出暴力的方法
        # 这样的话递归就很容易了，找到起点，所有的单个字符，和两个字符都是起始点
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][-1]

    def longest_palindrome_subseq_test(self):
        print(self.longest_palindrome_subseq("bbbab"))


if __name__ == "__main__":
    s = DpQuestion()
    s.longest_palindrome_subseq_test()
