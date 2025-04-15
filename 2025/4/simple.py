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


def main():
    s = Solution()
    print(s.count_good_triplets([3, 0, 1, 1, 9, 7], 7, 2, 3))


if __name__ == "__main__":
    main()
