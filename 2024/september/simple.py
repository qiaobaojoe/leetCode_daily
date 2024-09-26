from typing import List


class SimpleSolution:
    def difference_of_sum(self, nums: List[int]) -> int:

        sum_num = 0
        sum_digit = 0

        for num in nums:
            sum_num += num
            while num > 0:
                remaind = num % 10
                num //= 10
                sum_digit += remaind

        return abs(sum_num - sum_digit)


def main():
    solution = SimpleSolution()
    print(solution.difference_of_sum([1, 15, 6, 3]))
    # print(9 // 10)
    # print(9 % 10)


if __name__ == "__main__":
    main()
