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


def main():
    solution = Solution()
    print(solution.maximum_prime_difference([4, 2, 9, 5, 3]))


if __name__ == "__main__":
    main()
