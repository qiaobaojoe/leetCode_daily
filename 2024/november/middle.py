from itertools import count
from math import sqrt
from typing import List


class MiddleSolution:
    def count_complete_day_pairs(self, hours: List[int]) -> int:
        hours_remaind = {}
        for hour in hours:
            hours_remaind[(hour % 24)] = hours_remaind.get((hour % 24), 0) + 1
        ans = self.pairs_help(hours_remaind.get(0, 0)) + self.pairs_help(
            hours_remaind.get(12, 0)
        )
        for i in range(1, 12):
            ans += self.pairs_help_two(
                hours_remaind.get(i, 0), hours_remaind.get(24 - i, 0)
            )
        return ans

    def pairs_help(self, k: int) -> int:
        if k < 2:
            return 0
        if k == 2:
            return 1

        return k * (k - 1) // 2

    def pairs_help_two(self, k: int, n: int) -> int:
        if k == 0 or n == 0:
            return 0
        return n * k

    def judge_square_sum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l < r:
            if l * l + r * r == c:
                return True
            if l * l + r * r < c:
                l += 1
            else:
                r -= 1
        return False

    def results_array(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        ans = [-1] * (n - k + 1)
        constant_range = []
        # 找到所有 >= k的连续区间
        start, end = -1, -1
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                if start == -1:
                    start = i
                end = i + 1
                if i == n - 2:
                    constant_range.append((start, end))
            else:
                if start != -1 and end - start + 1 >= k:
                    constant_range.append((start, end))
                start, end = -1, -1
        if len(constant_range) == 0:
            return ans
        for s, e in constant_range:
            for i in range(s, e - k + 2):
                ans[i] = nums[i + k - 1]
        return ans

    def single_non_duplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, n - 1
        while r > l:
            m = (r + l) // 2
            if m % 2 != 0:
                if m < n - 2:
                    m += 1
                else:
                    m -= 1

            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                if nums[m] == nums[m - 1]:
                    r = m - 2
                else:
                    return nums[m]
        return nums[l]

    def count_k_constraint_substrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        # 枚举
        while n > 0:
            for i in range(len(s) - n + 1):
                sub_string = s[i : i + n :]
                if sub_string.count("0") <= k or sub_string.count("1") <= k:
                    ans += 1
            n -= 1

        return ans

    def count_good_nodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        node_count = [[] for _ in range(n)]
        for a, b in edges:
            node_count[a].append(b)
        ans = 0
        for node in node_count:
            if len(node) == 0 or len(node) == 1:
                ans += 1
            else:
                # 统计每一个子树所包含的节点数量
                child_count = [0] * len(node)

                for i, child in enumerate(node):
                    cur_stack = [child]
                    while len(cur_stack) > 0:
                        cur = cur_stack.pop()
                        child_count[i] += 1
                        for c in node_count[cur]:
                            cur_stack.append(c)

                child_count.sort()
                if child_count[0] == child_count[-1]:
                    ans += 1
        return ans

    def shortest_distance_after_queries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        ans = [0] * len(queries)
        grid = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            grid[i][i + 1] = 1

        for i, (a, b) in enumerate(queries):
            grid[a][b] = 1
            ans[i] = self.bfs_help(n, grid)
        return ans

    def bfs_help(self, n: int, grid: List[List[int]]) -> int:
        visited = [False] * n
        queue = [0]
        for step in count(1):
            tem = queue[::]
            queue = []
            while tem:
                cur = tem.pop()
                visited[cur] = True
                row = grid[cur]
                for j, r in enumerate(row):
                    if r == 1:
                        if j == n - 1:
                            return step
                        if not visited[j]:
                            queue.append(j)
        return -1

    def non_special_count(self, l: int, r: int) -> int:
        ans = 0
        for i in range(l, r + 1):
            if not self.is_special_num(i):
                ans += 1
        return ans

    def is_special_num(self, num: int) -> bool:
        cur = int(num**0.5)
        if cur * cur == num:
            return True
        return False


def main():
    solution = MiddleSolution()
    print(solution.non_special_count(4,16))


if __name__ == "__main__":
    main()
