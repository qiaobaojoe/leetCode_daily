from collections import deque
from typing import List


class Solution:

    def update_matrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [([-1] * n) for _ in range(m)]
        zero_deq = deque()
        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    zero_deq.append((y, x, 0))
                    ans[y][x] = 0
        drictions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while zero_deq:
            (y, x, d) = zero_deq.popleft()
            for dy, dx in drictions:
                cur_y, cur_x = y + dy, x + dx
                if cur_y < 0 or cur_x < 0 or cur_y >= m or cur_x >= n:
                    # 数组越界
                    continue
                if ans[cur_y][cur_x] == -1:
                    # 没有填充距离
                    ans[cur_y][cur_x] = d + 1
                    zero_deq.append((cur_y, cur_x, d + 1))

        return ans

    def update_matrix_test(self):
        print(self.update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

    def max_distance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        land_queue = deque()
        ans = [[-1] * n for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if grid[y][x] == 1:
                    ans[y][x] = 0
                    land_queue.append((y, x, 0))
        if len(land_queue) == 0 or len(land_queue) == n * n:
            # 全是海洋，或者全是陆地
            return -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_dis = 0
        while land_queue:
            (y, x, d) = land_queue.popleft()
            for dy, dx in directions:
                cur_y, cur_x = y + dy, x + dx
                if cur_x < 0 or cur_y < 0 or cur_x >= n or cur_y >= n:
                    # 数组越界
                    continue
                if ans[cur_y][cur_x] == -1:
                    # 距离尚未标定
                    cur_d = d + 1
                    ans[cur_y][cur_x] = cur_d
                    land_queue.append((cur_y, cur_x, cur_d))
                    max_dis = max(max_dis, cur_d)
        return max_dis

    def max_distance_test(self):
        print(self.max_distance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))


if __name__ == "__main__":
    s = Solution()
    s.max_distance_test()
