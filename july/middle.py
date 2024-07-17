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
            print(nums,low_pivot,i,high_pivot)
            while i <= high_pivot and nums[i] == 2:
                nums[i], nums[high_pivot] = nums[high_pivot], nums[i]
                high_pivot -= 1
            if nums[i] == 0:
                nums[i], nums[low_pivot] = nums[low_pivot], nums[i]
                low_pivot += 1
            i += 1


def main():
    solution = Soluton()
    ans = [2, 0, 1, 0, 1, 2, 1, 1, 2]
    solution.sort_colors(ans)
    print(ans)


if __name__ == "__main__":
    main()
