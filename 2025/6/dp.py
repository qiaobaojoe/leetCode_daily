from functools import cache
from typing import List


class DpQuestion:

    def rob(self, nums: List[int]) -> int:
        # rob(n+1) = rob(n)(0) + rob(n-1)(1)
        n = len(nums)
        if n < 2:
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
        f = [0] * (n + 1)
        # 初始状态复制 第一家偷了，第二家没有偷
        f[0] = 0
        f[1] = nums[1]

        for i in range(2, n):
            f[i] = max(nums[i] + f[i - 2], f[i - 1])
        return f[n - 1]

    def rob_test(self):
        print(self.rob([2, 1, 1, 2]))

    def delete_and_earn(self, nums: List[int]) -> int:
        # 强  转化成rob，太强了
        val_sum = [0] * (max(nums) + 1)
        for num in nums:
            val_sum[num] += num
        return self.rob(val_sum)

    def delete_and_earn_test(self):
        print(self.delete_and_earn([3, 4, 2]))

    def unique_paths(self, m: int, n: int) -> int:
        # 很直接的dp思路 f[m][n] = f[m-1][n] + f[m][n-1]
        dp = [[0] * n for _ in range(m)]
        for y in range(1, m):
            dp[y][0] = 1
        for x in range(1, n):
            dp[0][x] = 1
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[m - 1][n - 1]

    def unique_paths_test(self):
        print(self.unique_paths(3, 7))

    def min_falling_path_sum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(matrix[0]):
            dp[0][i] = x
        for i in range(1, n):
            for j in range(0, n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == n - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = matrix[i][j] + min(
                        dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j - 1]
                    )
        return min(dp[n - 1])

    def min_falling_path_sum_test(self):
        print(self.min_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))

    def maximal_square(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1:
            if matrix[0][0] == "1":
                return 1
            else:
                return 0
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        for x in range(n):
            if matrix[0][x] == "1":
                dp[0][x] = 1
                max_side = 1
        for y in range(1, m):
            if matrix[y][0] == "1":
                dp[y][0] = 1
                max_side = 1
        for y in range(1, m):
            for x in range(1, n):
                if matrix[y][x] == "1":
                    dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1]) + 1
                    max_side = max(max_side, dp[y][x])
        return max_side * max_side

    def maximal_square_test(self):
        print(
            self.maximal_square(
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            )
        )

    # 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
    def longest_palindrome_subseq(self, s: str) -> int:
        # dp没有思路，先上最暴力的解法，在面试的时候也是如此，如果没有刷过题目，找不好状态方程，直接给出暴力的方法
        # 这样的话递归就很容易了，找到起点，所有的单个字符，和两个字符都是起始点
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][-1]

    def longest_palindrome_subseq_test(self):
        print(self.longest_palindrome_subseq("bbbab"))

    def min_distance(self, word1: str, word2: str) -> int:
        # 这里我认为要分为三种情况去考虑
        # 1. word1 的长度和 word2 的长度相同，遍历两个字符，相同下标字符不同替换即可
        ans = 0
        len1, len2 = len(word1), len(word2)
        if len1 == len2:
            for l1, l2 in zip(word1, word2):
                if l1 != l2:
                    ans += 1
            return ans
        # 2. word1的长度大于word2的长度，需要找到两个字符串种 按顺序最多的公共相同字符
        # 这个情况有点困难了，不是先找到第一个相同，再去找下个相同的字符，可以选择从第二相同的字符开始 todo

        pass

    def min_distance_test(self):
        print(self.min_distance("horse", "ros"))

    def length_of_lis(self, nums: List[int]) -> int:
        # 数组最长子序列的问题，在推导子问题的过程中，最开始我陷入了一个误区
        # 对于求 i-1和i的关系，我认为一定是i比i-1里面所有的数据都大，才能得到ans(i-1)+1，
        # 这个推论是没有问题，但是他不能形成有效的递推关系，因为i不比i-1的所有数据都大，也是有可能序列加一，我没有办法推导出状态转移方程
        # 在看了题解后，明白了这个问题的解法，有一个重要的前提，就是子序列一定要选中最后一个元素，就会简化一部分遍历
        # 刚才理解了递归的写法，现在来推导一下动态规划，应该不难
        # 没有想到这个动态规划我完全没有思路
        # dp[i]代表 0-i范围内的数据，选择i作为的最后一位的最长子序列长度
        n = len(nums)
        dp = [1] * n
        # dp[i] 代表以下标i作为最后一个元素的最长子序列长度
        for i in range(1, n):
            max_length_i = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    max_length_i = max(max_length_i, dp[j] + 1)
            dp[i] = max_length_i
        return max(dp)

    def get_all_subsequences(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start: int, current: List[int]):
            # 每个当前序列都是一个有效的子序列
            subsequences.append(current[:])

            # 从start开始，避免重复
            for i in range(start, len(nums)):
                # 如果当前序列为空或者新数字大于序列最后一个数字
                if not current or nums[i] > current[-1]:
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()

        subsequences = []
        backtrack(0, [])
        return subsequences

    def length_of_lis_test(self):
        print(self.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))

    def letter_combinations(self, digits: str) -> List[str]:
        num_letter_table = [[] for _ in range(10)]
        num_letter_table[2] = ["a", "b", "c"]
        num_letter_table[3] = ["d", "e", "f"]
        num_letter_table[4] = ["g", "h", "i"]
        num_letter_table[5] = ["j", "k", "l"]
        num_letter_table[6] = ["m", "n", "o"]
        num_letter_table[7] = ["p", "q", "r", "s"]
        num_letter_table[8] = ["t", "u", "v"]
        num_letter_table[9] = ["w", "x", "y", "z"]

        ans = [""]
        for c in digits:
            letters = num_letter_table[int(c)]
            next_ans = []
            while ans:
                tem_s = ans.pop()
                for l in letters:
                    next_ans.append(tem_s + l)
            ans = next_ans
        return ans

    def letter_combinations_test(self):
        print(self.letter_combinations("23"))


if __name__ == "__main__":
    s = DpQuestion()
    s.length_of_lis_test()
