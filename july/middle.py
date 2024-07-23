from typing import List


class Soluton:

    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low_pivot = 0
        high_pivot = len(nums) - 1
        i = 0

        while i <= high_pivot:
            if nums[i] == 2:
                nums[i], nums[high_pivot] = nums[high_pivot], nums[i]
                high_pivot -= 1
                continue
            if nums[i] == 0:
                nums[i], nums[low_pivot] = nums[low_pivot], nums[i]
                low_pivot += 1
                i += 1
            elif nums[i] == 1:
                i += 1

        print(nums, low_pivot, high_pivot)

    def minimum_levels(self, possible: List[int]) -> int:
        remaind_count = 0
        for cur in possible:
            if cur == 0:
                remaind_count -= 1
            else:
                remaind_count += 1

        cur_count = 0
        for i, cur in enumerate(possible[: len(possible) - 1]):
            if cur == 0:
                cur_count -= 1
                remaind_count += 1
            else:
                cur_count += 1
                remaind_count -= 1
            if cur_count > remaind_count:
                return i + 1

        return -1


def main():
    solution = Soluton()
    ans = [1, 1]
    print(solution.minimum_levels(ans))


if __name__ == "__main__":
    main()
