from typing import List


class Solution:
    def check_two_chessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # 打印一个字母acII码
        a_1 = coordinate1[0]
        a_2 = int(coordinate1[1])

        b_1 = coordinate2[0]
        b_2 = int(coordinate2[1])

        ac_a_1 = int(ord(a_1))
        ac_b_1 = int(ord(b_1))

        if b_2 % 2 == a_2 % 2 and ac_a_1 % 2 == ac_b_1 % 2:
            return True

        if b_2 % 2 != a_2 % 2 and ac_a_1 % 2 != ac_b_1 % 2:
            return True

        return False

    def num_rook_captures(self, board: List[List[str]]) -> int:
        ans = 0
        # 找到R的位置
        r_i, r_j = 0, 0
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if "R" == val:
                    r_i = i
                    r_j = j
                    break
        # 前
        cur_row = board[r_i]
        for f in range(r_j - 1, -1, -1):
            if "p" == cur_row[f]:
                ans += 1
                break
            if "B" == cur_row[f]:
                break
        # 后
        for b in range(r_j, len(cur_row)):
            if "p" == cur_row[b]:
                ans += 1
                break
            if "B" == cur_row[b]:
                break
        # 上
        cur_line = []
        for i, _ in enumerate(board):
            cur_line.append(board[i][r_j])
        for u in range(r_j - 1, -1, -1):
            if "p" == cur_line[u]:
                ans += 1
                break
            if "B" == cur_line[u]:
                break
        # 下
        for d in range(r_j, len(cur_line)):
            if "p" == cur_line[d]:
                ans += 1
                break
            if "B" == cur_line[d]:
                break
        return ans

    def square_is_white(self, coordinates: str) -> bool:
        row = int(coordinates[1])
        col = int(ord(coordinates[0])) - 96
        return (row ^ col) & 1 == 1

    def semi_ordered_permutation(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        # 找到最大的
        if nums[n - 1] != n:
            swap_flag = False
            for i in range(n - 1):
                if nums[i] == n:
                    swap_flag = True
                if swap_flag:
                    if nums[i + 1] < nums[i]:
                        ans += 1
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # 找到1的位置
        if nums[0] != 1:
            swap_flag = False
            for j in range(n - 2, -1, -1):
                if nums[j + 1] == 1:
                    swap_flag = True
                if swap_flag:
                    if nums[j] > nums[j + 1]:
                        ans += 1
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return ans


def main():
    solution = Solution()
    print(solution.semi_ordered_permutation([3,2,4,1]))


if __name__ == "__main__":
    main()
