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


def main():
    solution = SortSolution()
    print(solution.select_sort([2, 4, 8, 9]))


if __name__ == "__main__":
    main()
