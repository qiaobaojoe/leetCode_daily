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


def main():
    solution = Solution()
    print(solution.check_two_chessboards("a1", "c3"))


if __name__ == "__main__":
    main()
