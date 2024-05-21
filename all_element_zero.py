import time
from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        print(length)
        diff = [0] * (length + 1)
        diff[0] = nums[0]
        for index, element in enumerate(nums[1:], start=1):
            diff[index] = element - nums[index - 1]
        print(diff)

        for i in range(length):
            if diff[i] == 0:
                continue
            if diff[i] < 0:
                return False
            if i + k > length:
                return False
            cur = diff[i]
            diff[i + k] += cur
        return True

    def maximumCount(self, nums: List[int]) -> int:
        posCount = 0
        negCount = 0

        for element in nums:
            if element > 0:
                posCount += 1
            if element < 0:
                negCount += 1
        if posCount > negCount:
            return posCount
        return negCount

    def maximumCountDichotomy(self, nums: List[int]) -> int:

        neg = self.searchLowBound(nums, 0)
        pos = self.searchLowBound(nums, 1)
        return max(neg, len(nums) - pos)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        range = [self.searchLowBound(nums, target), self.searchHighBound(nums, target)]
        return range

    def searchLowBound(self, nums: List[int], target: int) -> int:
        range = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            print("l={},r={},m={},val={}".format(l, r, m, nums[m]))
            if nums[m] < target:
                l = m + 1
                print("小于目标值 l={},r={}".format(l, r))
                continue
            if nums[m] == target:
                r = m - 1
                range = m
                print("等于目标值 l={},r={}".format(l, r))
                continue
            else:
                r = m - 1
                print("大于目标值 l={},r={}".format(l, r))

        if range == -1:
            range = l
        return range

    def searchHighBound(self, nums: List[int], target: int) -> int:
        range = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            print("l={},r={},m={},val={}".format(l, r, m, nums[m]))
            if nums[m] < target:
                l = m + 1
                print("小于目标值 l={},r={}".format(l, r))
                continue
            if nums[m] == target:
                l = m + 1
                range = m
                print("等于目标值 l={},r={}".format(l, r))
                continue
            else:
                r = m - 1
                print("大于目标值 l={},r={}".format(l, r))

        return range

    def minimizedStringLength(self, s: str) -> int:
        mask = 0
        print("a={}".format(ord("b")))
        for c in s:
            mask |= 1 << (ord(c) - ord("a"))
            print(bin(mask))
            print(mask)
        return bin(mask).count("1")

    def findChampion(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(grid):
            if row[ans] == 1:
                ans = i
        return ans

    def finalString(self, s: str) -> str:
        final = ""
        for c in s:
            if c != "i":
                final += c
            else:
                final = final[::-1]
        return final

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            print("------求解dp[{}]的最大组合------".format(i))
            for num in nums:
                if num <= i:
                    print("num={}:dp[{}] = dp[{}] + dp[{}]".format(num, i, i, i - num))
                    dp[i] = dp[i] + dp[i - num]
                    print(dp)
        return dp[target]

    def combinationSum4Recursion(self, nums: List[int], target: int) -> int:
        print("target={}".format(target))
        sum = 0
        for num in nums:
            print("当前for循环中num = {},target = {}".format(num, target))
            if num > target:
                print("num大于目标值,无法拆分")
                continue
            if num == target:
                sum += 1
                print("num==目标值,求和值加1")
                continue
            print("num小于目标值,继续拆分子问题,求最优解")
            sub = self.combinationSum4Recursion(nums, target - num)
            print(
                "递归结果返回 sum ={},target{}-num{} =nextTarget{},sub={}".format(
                    sum, target, num, target - num, sub
                )
            )
            sum = sum + sub
        return sum

    def combinationSum4RecursionMem(self, nums: List[int], target: int) -> int:
        mem = [-1] * (target + 1)
        self.combinationSum4RecursionMemSub(nums, target, mem)
        return mem[target]

    def combinationSum4RecursionMemSub(self, nums, target, mem):
        print("target={}".format(target))
        if mem[target] != -1:
            print("记忆表已经有存储{}".format(mem[target]))
            return mem[target]
        sum = 0
        for num in nums:
            print("当前for循环中num = {},target = {}".format(num, target))
            if num > target:
                print("num大于目标值,无法拆分")
                continue
            if num == target:
                sum += 1
                print("num==目标值,求和值加1")
                continue
            print("num小于目标值,继续拆分子问题,求最优解")
            sub = self.combinationSum4RecursionMemSub(nums, target - num, mem)
            print(
                "递归结果返回 sum ={},target{}-num{} =nextTarget{},sub={}".format(
                    sum, target, num, target - num, sub
                )
            )
            sum = sum + sub
        print("添加记忆表数据target={},val = {}".format(target, sum))
        mem[target] = sum
        return sum

    def change(self, amount: int, coins: List[int]) -> int:
        return 1


if __name__ == "__main__":
    # 调用 checkArray 方法并打印结果
    nums = [1, 2, 5]
    solution = Solution()
    methods = solution.change(5, nums)
    print(methods)

