from typing import List


class SearchSolution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


def main():
    solution = SearchSolution()
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))


if __name__ == "__main__":
    main()
