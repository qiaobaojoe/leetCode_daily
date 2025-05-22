from functools import lru_cache
from typing import List
import heapq


class State:
    def __init__(self, x, y, dis, steps=0):
        self.x = x
        self.y = y
        self.dis = dis
        self.steps = steps

    def __lt__(self, other):
        return self.dis < other.dis


class Solution:
    def network_delay_time(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[float("inf")] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        dist = [float("inf")] * n
        dist[k - 1] = 0
        used = [False] * n
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            print(x)
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float("inf") else -1

    def network_delay_time_heap(self, times: List[List[int]], n: int, k: int) -> int:
        # 构建邻接表
        g = [[] for _ in range(n)]
        for x, y, time in times:
            g[x - 1].append((y - 1, time))
        dist = [float("inf")] * n
        dist[k - 1] = 0
        # 构建小根堆
        heap = [(0, k - 1)]

        while heap:
            time, x = heapq.heappop(heap)
            if time > dist[x]:
                continue
            for y, time in g[x]:
                if dist[y] > dist[x] + time:
                    dist[y] = dist[x] + time
                    heapq.heappush(heap, (dist[y], y))
        ans = max(dist)
        return ans if ans < float("inf") else -1

    def min_time_to_reach(self, move_time: List[List[int]]) -> int:
        n = len(move_time)  # y 的长度
        m = len(move_time[0])  # x 的长度
        dists = [[float("inf")] * m for _ in range(n)]
        vistied = [[0] * m for _ in range(n)]
        # 每个坐标的邻接矩阵
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dists[0][0] = 0
        heap = [State(0, 0, 0)]
        while heap:
            s = heapq.heappop(heap)
            x, y, d = s.x, s.y, s.dis
            if vistied[y][x]:
                continue
            vistied[y][x] = 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= ny < n and 0 <= nx < m):
                    continue
                dist = max(d, move_time[ny][nx]) + 1
                if dist < dists[ny][nx]:
                    dists[ny][nx] = dist
                    heapq.heappush(heap, State(nx, ny, dist))

        return dists[n - 1][m - 1]

    def min_time_to_reach_v2(self, move_time: List[List[int]]) -> int:
        n = len(move_time)  # y的长度
        m = len(move_time[0])  # x的长度
        dists = [[float("inf")] * m for _ in range(n)]
        vistied = [[0] * m for _ in range(n)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dists[0][0] = 0
        heap = [State(0, 0, 0)]

        while heap:
            s = heapq.heappop(heap)
            x, y, d, steps = s.x, s.y, s.dis, s.steps
            if vistied[y][x] == 1:
                continue
            vistied[y][x] = 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                cur_d = max(d, move_time[ny][nx]) + 1 + (0 if steps % 2 == 0 else 1)
                if cur_d < dists[ny][nx]:
                    heapq.heappush(heap, State(nx, ny, cur_d, steps + 1))
                    dists[ny][nx] = cur_d
        return dists[n - 1][m - 1]

    def min_sum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        count_zero1 = nums1.count(0)
        sum2 = sum(nums2)
        count_zero2 = nums2.count(0)
        min_sum1 = sum1 + count_zero1
        max_sum1 = sum1 + count_zero1 * 10**100
        min_sum2 = sum2 + count_zero2
        max_sum2 = sum2 + count_zero2 * 10**100

        if min_sum1 > max_sum2 or min_sum2 > max_sum1:
            return -1
        return max(min_sum1, min_sum2)

    def length_after_transformations(self, s: str, t: int) -> int:
        # dp大法真的优雅，列出顶顶有名的状态转移方程 i 代表转换的次数 j代表字母
        # f[i][j] = f[i-1][j-1]  j-1 = z 时需要特殊处理，会产生分裂
        # f[i][a] = f[i-1][z] f[i][b] = f[i][b] + f[i-1][z]
        # 列出状态数组
        dp = [[0] * 26 for _ in range(t + 1)]
        # 初始化状态  t=0
        for c in s:
            ac_c = ord(c) - 97
            dp[0][ac_c] += 1

        for i in range(1, t + 1):
            for j in range(1, 26):
                dp[i][j] = dp[i - 1][j - 1]
            dp[i][0] = dp[i - 1][25]
            dp[i][1] += dp[i - 1][25]

        return sum(dp[t]) % (10**9 + 7)

    def length_after_transformations2(self, s: str, t: int, nums: List[int]) -> int:
        # dp大法真的优雅，列出顶顶有名的状态转移方程 i 代表转换的次数 j代表字母
        # 这个状态转移方程式比较难列的，需要遍历nums的数组才能得到
        # f[i][j] = f[i-1][x] x代表有多个字母可以转移成j
        # 列出状态数组
        dp = [[0] * 26 for _ in range(t + 1)]
        # 初始化状态  t=0
        for c in s:
            ac_c = ord(c) - 97
            dp[0][ac_c] += 1

        for i in range(1, t + 1):
            for j in range(0, 26):
                transform_index = self.transform_j_index(j, tuple(nums))
                for t_i in transform_index:
                    dp[i][j] += dp[i - 1][t_i]

        return sum(dp[t]) % (10**9 + 7)

    @lru_cache(maxsize=128, typed=False)
    def transform_j_index(self, j: int, nums: tuple) -> List[int]:
        ans = []
        for i in range(1, 26):
            cur = i + j
            if cur < 26:
                if (nums[cur] + cur) > 25:
                    if nums[cur] + cur - 26 >= j:
                        ans.append(cur)
            else:
                cur -= 26
                if nums[cur] + cur >= j:
                    ans.append(cur)
        return ans

    def get_words_in_longest_subsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        def check(s: str, t: str) -> bool:
            return len(s) == len(t) and sum(x != y for x, y in zip(s, t)) == 1

        n = len(words)
        f = [0] * n
        from_ = [0] * n
        max_i = n - 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 提前比较 f[j] 与 f[i] 的大小，如果 f[j] <= f[i]，就不用执行更耗时的 check 了
                if f[j] > f[i] and groups[j] != groups[i] and check(words[i], words[j]):
                    f[i] = f[j]
                    from_[i] = j
            f[i] += 1  # 加一写在这里
            if f[i] > f[max_i]:
                max_i = i

        i = max_i
        ans = [""] * f[i]
        for k in range(f[i]):
            ans[k] = words[i]
            i = from_[i]
        return ans

    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p0 = 0, 0
        for i, num in enumerate(nums):
            nums[i] = 2
            if num <= 1:
                nums[p1] = 1
                p1 += 1
            if num == 0:
                nums[p0] = 0
                p0 += 1

    def is_zero_array(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff_arry = [0] * (len(nums) + 1)
        diff_arry[0] = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            diff_arry[i] = num - nums[i - 1]
        for l, r in queries:
            diff_arry[l] -= 1
            diff_arry[r + 1] += 1
        diff_sum = 0
        for diff in diff_arry[: len(nums) :]:
            diff_sum += diff
            if diff_sum > 0:
                return False
        return True

    def is_zero_array_test(self):
        print(self.is_zero_array([0, 5], [[1, 1]]))

    def car_pooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 对trips 进行排序
        ans = [0] * 1001
        for p, f, t in trips:
            ans[f] += p
            # t已经下车了，是把 到t-1区间内+p
            ans[t] -= p
        p_count = 0
        for a in ans:
            p_count += a
            if p_count > capacity:
                return False
        return True

    def car_pooling_test(self):
        print(self.car_pooling([[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]], 23))

    def min_zero_array2(self, nums: List[int], queries: List[List[int]]) -> int:
        if nums.count(0) == len(nums):
            return 0

        def check(k: int) -> bool:
            n = len(nums)
            diffs = [0] * (n + 1)
            diffs[0] = nums[0]
            for i, num in enumerate(nums):
                if i == 0:
                    continue
                diffs[i] = num - nums[i - 1]
            for l, r, v in queries[: k + 1 :]:
                diffs[l] -= v
                diffs[r + 1] += v
            cur_sum = 0
            for i, d in enumerate(diffs):
                if i == n:
                    continue
                cur_sum += d
                if cur_sum > 0:
                    return False
            return True

        # 二分查找区间
        left, right = 0, len(queries) - 1
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            print(mid)
            if check(mid):
                right = mid
            else:
                left = mid + 1
        print(left, right)
        if check(left):
            return left + 1
        return -1

    def min_zero_array_test2(self):
        self.min_zero_array2([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]])

    def search_range(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def low_bound(cur_target) -> int:
            # 开区间方法
            li = -1
            ri = len(nums)
            while li + 1 < ri:
                mi = li + (ri - li) // 2
                if nums[mi] >= cur_target:
                    ri = mi
                else:
                    li = mi
            return li + 1

        # 这里返回的是Left,也就是Left左边的肯定都会比left小。当left = 0 的时候需要判断 left是否 == target，如果不等于就是没有找到
        left_bound = low_bound(target)
        if left_bound == len(nums):
            return [-1, -1]
        if nums[left_bound] != target:
            return [-1, -1]
        return [left_bound, low_bound(target + 1) - 1]

    def search_range_test(self):
        print(self.search_range([2,2], 3))
        print(self.search_range([5, 7, 7, 8, 8, 10], 8))
        print(self.search_range([5, 7, 7, 8, 8, 10], 7))


if __name__ == "__main__":
    s = Solution()
    s.search_range_test()
