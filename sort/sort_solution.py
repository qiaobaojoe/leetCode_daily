from typing import List


class Sortsolution:

    def select_sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

    def bubble_sort(self, nums: List[int]) -> List[int]:
        switch_flag = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    switch_flag += 1
            if switch_flag == 0:
                return nums
        return nums

    def insert_sort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            cur = nums[i]
            for j in range(i):
                if cur < nums[j]:
                    self.move_one(nums, i, j)
                    nums[j] = cur
                    break
        return nums

    def move_one(self, nums: List[int], i: int, j: int):
        while i > j:
            nums[i] = nums[i - 1]
            i -= 1

    def quick_sort(self, nums: List[int]) -> List[int]:
        self.quick_sort_help(nums, 0, len(nums) - 1)
        return nums

    def quick_sort_help(self, nums: List[int], left: int, right: int):
        if left >= right:
            return
        pivot = self.quick_sort_partion(nums, left, right)
        self.quick_sort_help(nums, pivot + 1, right)
        self.quick_sort_help(nums, left, pivot - 1)

    def quick_sort_partion(self, nums: List[int], left: int, right: int) -> int:
        print(nums,left,right)
        pivot = left
        base_num = self.find_base_num(nums, left, right)
        i, j = left, right
        while i <= j:
            if nums[i] < base_num:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                i += 1
                pivot += 1
                continue
            if nums[i] > base_num:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
                continue
            i += 1
        print(nums,pivot)
        return pivot

    def find_base_num(self, nums, left, right) -> int:
        middle = (left + right) // 2
        left_num = nums[left]
        right_num = nums[right]
        middle_num = nums[middle]
        base_num = left_num
        if (left_num <= middle_num <= right_num) or (
            right_num <= middle_num <= left_num
        ):
            base_num = middle_num
        if (left_num <= right_num <= middle_num) or (
            middle_num <= right_num <= left_num
        ):
            base_num = right_num
        return base_num


def main():
    solution = Sortsolution()
    nums = [5, 2, 3, 1, 8, 36, 6, 7, 78, 8]
    print(solution.quick_sort(nums))


if __name__ == "__main__":
    main()
