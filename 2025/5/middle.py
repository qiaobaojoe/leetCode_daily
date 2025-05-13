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
        mod = 10**9 + 7
        dp = [[0] * 26 for _ in range(t + 1)]
        # dp[i][j] 表示字母j在第i次变换之后的长度
        # 初始化
        for c in s:
            dp[0][ord(c) - ord("a")] += 1
        # dp
        for i in range(1, t + 1):
            # 先处理a-y 对后面的影响
            for j in range(25):
                dp[i][j + 1] = dp[i - 1][j]
            # 单独处理 z 对 a 和 b 的影响
            dp[i][0] = dp[i - 1][25]
            dp[i][1] += dp[i - 1][25]

        total = 0
        for j in range(26):
            total = (total + dp[t][j]) % mod
        return total


def main():
    s = Solution()
    # print(s.network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(s.length_after_transformations("jqktcurgdvlibczdsvnsg", 7517))
    print(79033769)
    # print(s.min_time_to_reach([[0, 4], [4, 4]]))


if __name__ == "__main__":
    main()
