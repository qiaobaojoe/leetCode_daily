from collections import deque
from string import ascii_lowercase
from typing import List


class Solution:
    def smallest_equivalent_string(self, s1: str, s2: str, base_str: str) -> str:
        fa = {c: c for c in ascii_lowercase}

        def find(x: str) -> str:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def merge(x: str, y: str) -> None:
            small, big = sorted((find(x), find(y)))
            fa[big] = small  # 把大的代表元指向小的代表元

        for x, y in zip(s1, s2):
            merge(x, y)

        return "".join(find(c) for c in base_str)

    def smallest_equivalent_string_test(self):
        print(self.smallest_equivalent_string("leetcode", "programs", "sourcecode"))

    def robot_with_string(self, s: str) -> str:
        p, t = [], []
        s_list = deque()
        for c in s:
            s_list.append(c)
        while s_list:
            cur = s_list.popleft()
            while t:
                t_last = t[-1]
                if ord(t_last) >= ord(cur):
                    break
                p.append(t.pop())
            t.append(cur)
        while t:
            p.append(t.pop())

        return "".join(p)

    def robot_with_string_test(self):
        print(self.robot_with_string("bdda"))

    def clear_stars(self, s: str) -> str:
        stack = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == "*":
                for c_s in stack:
                    if c_s:
                        c_s.pop()
                        break
            else:
                stack[ord(c) - ord("a")].append(i)
        ans = [""] * len(s)
        for index, c_s in enumerate(stack):
            if c_s:
                for i in c_s:
                    ans[i] = chr(index + ord("a"))
        return "".join(ans)

    def clear_stars_test(self):
        print(self.clear_stars("aaba*"))

    def longest_palindrome(self, s: str) -> str:
        # 子字符串为最长回文字符串的最大长度一题
        # 确认边界条件 1<= len
        # 长度为1的字段都是回文字符串
        n = len(s)
        if n == 1:
            return s[0]
        # 长度为2的回文字符串只有可能是两个字符相等
        # 我的思路 遍历找到 长度为2的回文字符串和所有长度为1的字符串（都为回文字符串），以这些节点为启动，判断左右字符是否相等，相等就是组成新的回文字符串，再次参与迭代，
        # 中心发散的思路，有些类型深度搜索，但是每个节点的迭代发散都是独立的，没有剪枝
        # 哈哈 看了题解，我这么做就可以了 这里官方给出题解是递归的方式，但是我刚才的思路，应该迭代更直接一点
        palindrome_nodes = deque()
        for i in range(n):
            palindrome_nodes.append((i, i))
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome_nodes.append((i, i + 1))
        max_len = 0
        start_i = 0
        while palindrome_nodes:
            (l, r) = palindrome_nodes.popleft()
            if max_len < (r - l + 1):
                max_len = r - l + 1
                start_i = l
            if l == 0 or r == n - 1:
                continue
            if s[l - 1] == s[r + 1]:
                palindrome_nodes.append((l - 1, r + 1))

        return s[start_i : start_i + max_len]

    def longest_palindrome_test(self):
        print(self.longest_palindrome("cbbd"))

    def word_break(self, s: str, word_dict: List[str]) -> bool:
        n = len(s)
        sub_grid = [[0] * n for _ in range(n)]
        for word in word_dict:
            m = len(word)
            if m > n:
                continue
            for i in range(n - m + 1):
                sub = s[i : i + m]
                if sub == word:
                    sub_grid[i][i + m - 1] = 1
        # 到这一步已经把题目转化成几根棍子的问题了，在这里好像可以用到动态规划的思想了
        # 比较经典的要或者不要的场景
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j, arrived in enumerate(sub_grid[i]):
                if arrived:
                    dp[j + 1] = dp[j + 1] | dp[i]
        return dp[n]

    def word_break_test(self):
        print(self.word_break("aaaaaaa", ["aaaa", "aaa"]))

    def min_max_difference(self, num: int) -> int:
        s = str(num)
        max_s = []
        d1 = ""
        for c in s:
            if d1 == "":
                if c != "9":
                    d1 = c

            if c == d1:
                max_s.append("9")
            else:
                max_s.append(c)
        num_max = int("".join(max_s))
        min_s = []
        d3 = ""
        for c in s:
            if d3 == "":
                d3 = c
            if c == d3:
                if min_s:
                    min_s.append("0")
            else:
                min_s.append(c)
        if min_s:
            num_min = int("".join(min_s))
        else:
            num_min = 0

        return num_max - num_min

    def min_max_difference_test(self):
        print(self.min_max_difference(11891))


def main():
    s = Solution()
    s.min_max_difference_test()


if __name__ == "__main__":
    main()
