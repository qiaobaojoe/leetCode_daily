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


def main():
    solution = Soluton()
    ans = [0,0]
    solution.sort_colors(ans)
    print(ans)


if __name__ == "__main__":
    main()
