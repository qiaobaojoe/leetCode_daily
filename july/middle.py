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

    def relocate_marbles(
        self, nums: List[int], move_from: List[int], move_to: List[int]
    ) -> List[int]:
        marbles_map = {}
        ans = []
        for num in nums:
            marbles_map[num] = True
        move_len = len(move_from)
        for i in range(move_len):
            from_pos = move_from[i]
            to_pos = move_to[i]

            del marbles_map[from_pos]
            marbles_map[to_pos] = True

        ans = list(marbles_map.keys())
        ans.sort()
        return ans


def main():
    solution = Soluton()
    print(solution.relocate_marbles([1, 6, 7, 8], [1, 7, 2], [2, 9, 5]))
    print(solution.relocate_marbles([1, 1, 3, 3], [1, 3], [2, 2]))


if __name__ == "__main__":
    main()
