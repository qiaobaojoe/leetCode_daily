from typing import List


class Solution:
    def maximum_prime_difference(self, nums: List[int]) -> int:
        primes = {
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        }
        first, last = -1, 0
        for i, cur in enumerate(nums):
            if cur in primes:
                if first == -1:
                    first = i
                    last = i
                else:
                    last = i
        return last - first

    def sum_of_the_digits_of_harshad_number(self, x: int) -> int:
        str_x = str(x)
        sum_c = 0
        for cur in str_x:
            sum_c += int(cur)
        if x % sum_c == 0:
            return sum_c
        return -1

    def pivot_index(self, nums: List[int]) -> int:
        sum_all = sum(nums)
        sum_left = 0
        for i, val in enumerate(nums):
            if sum_left == (sum_all - val - sum_left):
                return i
            sum_left += val
        return -1

    def incremovable_subarray_count(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        ans = 3
        # 任一数量>=2的数组都至少包含三个移除递增子数组：包含自身全部元素的，去除头尾连个元素的
        # 考虑移除后递增子数组的size = 2
        subarray_size = len(nums) - 2
        while subarray_size > 0:
            for i in range(len(nums) - subarray_size+1):
                if self.is_incremovable(nums, i, subarray_size):
                    ans += 1
            subarray_size -= 1
        return ans

    def is_incremovable(self, nums: List[int], i: int, subarray_size: int) -> bool:
        if i == 0:
            cur = nums[subarray_size]
            for j in range(subarray_size + 1, len(nums)):
                if nums[j] > cur:
                    cur = nums[j]
                else:
                    return False

            return True

        cur = nums[0]
        for j in range(1, i):
            if nums[j] > cur:
                cur = nums[j]
            else:
                return False

        for j in range(subarray_size + i, len(nums)):
            if nums[j] > cur:
                cur = nums[j]
            else:
                return False

        return True


def main():
    solution = Solution()
    print(solution.incremovable_subarray_count([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
