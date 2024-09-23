from typing import List


class Solution:
    def max_score_sightseeing_pair(self, values: List[int]) -> int:
        max_score = 0
        size = len(values)
        for i, val_i in enumerate(values[: size - 1 :]):
            for j in range(i + 1, size):
                val_j = values[j]
                cur_score = val_i + val_j + i - j
                if cur_score > max_score:
                    max_score = cur_score
        return max_score


def main():
    # values = [8, 1, 5, 2, 6]
    # print(values[: len(values) - 1 :])
    solution = Solution()
    print(solution.max_score_sightseeing_pair([8, 1, 5, 2, 6]))


if __name__ == "__main__":
    main()
