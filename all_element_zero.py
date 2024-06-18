from typing import List


class Solution:
    def check_array(self, nums: List[int], k: int) -> bool:
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

    def maximum_count(self, nums: List[int]) -> int:
        pos_count = 0
        neg_count = 0

        for element in nums:
            if element > 0:
                pos_count += 1
            if element < 0:
                neg_count += 1
        if pos_count > neg_count:
            return pos_count
        return neg_count

    def maximum_count_dichotomy(self, nums: List[int]) -> int:

        neg = self.search_low_bound(nums, 0)
        pos = self.search_low_bound(nums, 1)
        return max(neg, len(nums) - pos)

    def search_range(self, nums: List[int], target: int) -> List[int]:
        return [self.search_low_bound(nums, target), self.search_high_bound(nums, target)]

    def search_low_bound(self, nums: List[int], target: int) -> int:
        bound_range = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            print(f"l={l},r={r},m={m},val={ nums[m]}")
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                r = m - 1
                bound_range = m
                continue
            else:
                r = m - 1

        if bound_range == -1:
            bound_range = l
        return bound_range

    def search_high_bound(self, nums: List[int], target: int) -> int:
        range = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] < target:
                l = m + 1
                continue
            if nums[m] == target:
                l = m + 1
                range = m
                continue
            else:
                r = m - 1

        return range

    def minimized_string_length(self, s: str) -> int:
        mask = 0
        for c in s:
            mask |= 1 << (ord(c) - ord("a"))
            print(bin(mask))
            print(mask)
        return bin(mask).count("1")

    def find_champion(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(grid):
            if row[ans] == 1:
                ans = i
        return ans

    def final_string(self, s: str) -> str:
        final = ""
        for c in s:
            if c != "i":
                final += c
            else:
                final = final[::-1]
        return final

    def combination_sum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] = dp[i] + dp[i - num]
                    print(dp)
        return dp[target]

    def combination_sum4_recursion(self, nums: List[int], target: int) -> int:
        sum = 0
        for num in nums:
            if num > target:
                print("num大于目标值,无法拆分")
                continue
            if num == target:
                sum += 1
                print("num==目标值,求和值加1")
                continue
            print("num小于目标值,继续拆分子问题,求最优解")
            sub = self.combination_sum4_recursion(nums, target - num)
            sum = sum + sub
        return sum

    def combination_sum4_recursion_mem(self, nums: List[int], target: int) -> int:
        mem = [-1] * (target + 1)
        self.combination_sum4_recursion_mem_sub(nums, target, mem)
        return mem[target]

    def combination_sum4_recursion_mem_sub(self, nums, target, mem):
        if mem[target] != -1:
            return mem[target]
        sum = 0
        for num in nums:
            if num > target:
                continue
            if num == target:
                sum += 1
                print("num==目标值,求和值加1")
                continue
            print("num小于目标值,继续拆分子问题,求最优解")
            sub = self.combination_sum4_recursion_mem_sub(nums, target - num, mem)
            sum = sum + sub
        mem[target] = sum
        return sum



if __name__ == "__main__":
    # 调用 checkArray 方法并打印结果
    nums = [1, 2, 5]
    solution = Solution()
    print(solution.change(5, nums))
