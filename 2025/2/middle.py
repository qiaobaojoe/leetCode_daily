from typing import List


# 这个类是2月份中等难度leetcode算法的实现
class Solution:
    def max_distance(self, arrays: List[List[int]]) -> int:
        # 暴力解法，遍历所有可能的组合，计算距离
        m = len(arrays)
        ans_arrays = [[] for _ in range(m)]
        for i, nums in enumerate(arrays):
            ans_arrays[i].append(nums[0])
            ans_arrays[i].append(nums[-1])
        ans = 0
        for i, a in enumerate(ans_arrays):
            for j in range(m):
                if i == j:
                    continue
                ans = max(ans, abs(a[0] - ans_arrays[j][1]))
        return ans


# 主程序入口
if __name__ == "__main__":
    solution = Solution()
    print(solution.max_distance([[1, 2, 3], [4, 5], [1, 2, 3]]))
