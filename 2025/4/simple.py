from typing import List


class Solution:
    def count_good_triplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 暴力枚举
        ans = 0
        n = len(arr)
        for i in range(n - 2):
            cur_j_arr, cur_k_arr = [-1] * n, [-1] * n
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    cur_j_arr[j] = arr[j]
            for k in range(i + 2, n):
                if abs(arr[i] - arr[k]) <= c:
                    cur_k_arr[k] = arr[k]

            for index, cur_j in enumerate(cur_j_arr):
                if cur_j == -1:
                    continue
                for cur_k in cur_k_arr[index + 1 : :]:
                    if cur_k == -1:
                        continue
                    if abs(cur_j - cur_k) <= b:
                        ans += 1

        return ans

    def count_pairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            val = nums[i]
            for j in range(i + 1, len(nums)):
                val_j = nums[j]
                if val == val_j and (i * j) % k == 0:
                    print(i, j)
                    ans += 1
        return ans


def main():
    s = Solution()
    print(s.count_pairs([5, 5, 9, 2, 5, 5, 9, 2, 2, 5, 5, 6, 2, 2, 5, 2, 5, 4, 3], 7))


if __name__ == "__main__":
    main()
