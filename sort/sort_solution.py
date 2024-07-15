from typing import List


class SortSolution:

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


def main():
    solution = SortSolution()
    print(solution.insert_sort([-2, 3, -5]))


if __name__ == "__main__":
    main()
