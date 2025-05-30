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

    def image_smoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(img):
            for j, val in enumerate(row):
                cur_sum = val
                cur_count = 1
                if i - 1 >= 0:
                    cur_sum += img[i - 1][j]
                    cur_count += 1
                if i + 1 < m:
                    cur_sum += img[i + 1][j]
                    cur_count += 1
                if j - 1 >= 0:
                    cur_sum += img[i][j - 1]
                    cur_count += 1
                if j + 1 < n:
                    cur_sum += img[i][j + 1]
                    cur_count += 1
                if i - 1 >= 0 and j - 1 >= 0:
                    cur_sum += img[i - 1][j - 1]
                    cur_count += 1
                if i - 1 >= 0 and j + 1 < n:
                    cur_sum += img[i - 1][j + 1]
                    cur_count += 1
                if i + 1 < m and j - 1 >= 0:
                    cur_sum += img[i + 1][j - 1]
                    cur_count += 1
                if i + 1 < m and j + 1 < n:
                    cur_sum += img[i + 1][j + 1]
                    cur_count += 1
                ans[i][j] = cur_sum // cur_count
        return ans

    def final_position_of_snake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0
        for c in commands:
            if "DOWN" == c:
                i += 1
            if "UP" == c:
                i -= 1
            if "RIGHT" == c:
                j += 1
            if "LEFT" == c:
                j -= 1

        return (i * n) + j

    def winning_player_count(self, n: int, pick: List[List[int]]) -> int:
        ans = 0
        # 最多只会有10种颜色的球，构建二维数组统计对于一个玩家各种颜色球的数量
        player_count = [[0] * 11 for _ in range(n)]
        for (x,y) in pick:
            player_count[x][y] += 1
        for (i,count) in enumerate(player_count):
            for c in count:
                if c > i:
                    ans += 1
                    break
        return ans
        
    def can_alice_win(self, nums: List[int]) -> bool:
        single_digit_sum,double_digit_sum = 0,0
        for n in nums:
            if n < 10:
                single_digit_sum += n
            else:
                double_digit_sum += n
        if single_digit_sum == double_digit_sum:
            return False
        return True


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
    solution = Simplesolution()
    print(solution.can_alice_win([1,2,3,4,10]))


if __name__ == "__main__":
    main()
