class MiddleSolution:
    def __init__(self) -> None:
        self.memo = {}

    def knight_probability(self, n: int, k: int, row: int, column: int) -> float:
        if self.memo.get((k, row, column)):
            return self.memo.get((k, row, column))
        if row < 0 or row >= n or column < 0 or column >= n:
            self.memo[(k, row, column)] = 0
            return 0
        if k == 0:
            self.memo[(k, row, column)] = 1
            return 1
        probablility = 0

        # 每一步有8个方向可以走
        # 上2
        probablility += self.knight_probability(n, k - 1, row - 2, column - 1) / 8
        probablility += self.knight_probability(n, k - 1, row - 2, column + 1) / 8
        # 上1
        probablility += self.knight_probability(n, k - 1, row - 1, column - 2) / 8
        probablility += self.knight_probability(n, k - 1, row - 1, column + 2) / 8
        # 下2
        probablility += self.knight_probability(n, k - 1, row + 2, column - 1) / 8
        probablility += self.knight_probability(n, k - 1, row + 2, column + 1) / 8
        # 下1
        probablility += self.knight_probability(n, k - 1, row + 1, column - 2) / 8
        probablility += self.knight_probability(n, k - 1, row + 1, column + 2) / 8

        self.memo[(k, row, column)] = probablility
        return probablility


def main():
    solution = MiddleSolution()
    print(solution.knight_probability(3, 2, 0, 0))
    # print(solution.knight_probability(8, 30, 6, 4))


if __name__ == "__main__":
    main()
