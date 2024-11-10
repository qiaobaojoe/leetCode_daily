from typing import List


class Simplesolution:
    def min_changes(self, n: int, k: int) -> int:
        if n == k:
            return 0
        if n < k:
            return -1
        binary_n = bin(n)[2::]
        binary_k = bin(k)[2::]
        if len(binary_n) != len(binary_k):
            binary_k = binary_k.zfill(len(binary_n))
        ans = 0
        for i, n_i in enumerate(binary_n):
            if n_i != binary_k[i]:
                if n_i == "1":
                    ans += 1
                else:
                    return -1
        return ans

    def losing_player(self, x: int, y: int) -> int:
        is_a = True
        for _ in range(1, x + 2):
            y -= 4
            if y < 0:
                is_a = not is_a
                break
            is_a = not is_a
        return "Alice" if is_a else "Bob"


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacent_sum(self, value: int) -> int:
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val == value:
                    return self.get_adjacent_sum(i, j)
        return -1

    def get_adjacent_sum(self, i: int, j: int) -> int:
        ans = 0
        # 上
        if i - 1 >= 0:
            ans += self.grid[i - 1][j]
        # 下
        if i + 1 < len(self.grid):
            ans += self.grid[i + 1][j]
        # 左
        if j - 1 >= 0:
            ans += self.grid[i][j - 1]
        # 右
        if j + 1 < len(self.grid[0]):
            ans += self.grid[i][j + 1]
        return ans

    def diagonal_sum(self, value: int) -> int:
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val == value:
                    return self.get_diagonal_sum(i, j)
        return -1

    def get_diagonal_sum(self, i: int, j: int) -> int:
        ans = 0
        # 左上
        if i - 1 >= 0 and j - 1 >= 0:
            ans += self.grid[i - 1][j - 1]
        # 左下
        if i + 1 < len(self.grid) and j - 1 >= 0:
            ans += self.grid[i + 1][j - 1]
        # 右上
        if i - 1 >= 0 and j + 1 < len(self.grid):
            ans += self.grid[i - 1][j + 1]
        # 右下
        if i + 1 < len(self.grid) and j + 1 < len(self.grid):
            ans += self.grid[i + 1][j + 1]
        return ans


def main():
    solution = NeighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(solution.adjacent_sum(1))
    print(solution.adjacent_sum(4))
    print(solution.diagonal_sum(4))
    print(solution.diagonal_sum(9))


if __name__ == "__main__":
    main()
