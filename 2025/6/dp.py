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
        return dp[m-1][n-1]

    def unique_paths_test(self):
        print(self.unique_paths(3, 7))


if __name__ == "__main__":
    s = DpQuestion()
    s.unique_paths_test()
