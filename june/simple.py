from typing import List


class SimpleSolution:

    def count_beautiful_pairs(self, nums: List[int]) -> int:
        """
        怎么确认两个数互为质数,不过值的范围在[1-9]之间,还是可以枚举的
        """
        beautiful_pair_map = {
            1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [1, 3, 5, 7, 9],
            3: [1, 2, 4, 5, 7, 8],
            4: [1, 3, 5, 7, 9],
            5: [1, 2, 3, 4, 6, 7, 8, 9],
            6: [1, 5, 7],
            7: [1, 2, 3, 4, 5, 6, 8, 9],
            8: [1, 3, 5, 7, 9],
            9: [1, 2, 4, 5, 7, 8],
        }
        count = 0
        for i in range(len(nums) - 1):
            first_digit = int(str(nums[i])[0])
            for j in range(i + 1, len(nums)):
                last_digit = nums[j] % 10
                beautiful_pairs = beautiful_pair_map[first_digit]
                if last_digit in beautiful_pairs:
                    count += 1

        return count


def main():

    solution = SimpleSolution()
    print(solution.count_beautiful_pairs([2, 5, 1, 4]))


if __name__ == "__main__":
    main()
