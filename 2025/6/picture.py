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


if __name__ == "__main__":
    s = Solution()
    s.update_matrix_test()
