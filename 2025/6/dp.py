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


if __name__ == "__main__":
    s = DpQuestion()
    s.delete_and_earn_test()
