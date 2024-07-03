from typing import List


class Solution:
    def maximum_prime_difference(self, nums: List[int]) -> int:
        primes = {
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        }
        first, last = -1, 0
        for i, cur in enumerate(nums):
            if cur in primes:
                if first == -1:
                    first = i
                    last = i
                else:
                    last = i
        return last - first

    def sum_of_the_digits_of_harshad_number(self, x: int) -> int:
        str_x = str(x)
        sum_c = 0
        for cur in str_x:
            sum_c += int(cur)
        if x % sum_c == 0:
            return sum_c
        return -1


def main():
    solution = Solution()
    print(solution.sum_of_the_digits_of_harshad_number(18))


if __name__ == "__main__":
    main()
