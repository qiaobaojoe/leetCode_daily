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


if __name__ == "__main__":
    s = DpQuestion()
    s.min_falling_path_sum_test()
