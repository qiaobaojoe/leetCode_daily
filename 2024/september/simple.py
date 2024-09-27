from typing import List


class SimpleSolution:
    def difference_of_sum(self, nums: List[int]) -> int:

        sum_num = 0
        sum_digit = 0

        for num in nums:
            sum_num += num
            while num > 0:
                remaind = num % 10
                num //= 10
                sum_digit += remaind

        return abs(sum_num - sum_digit)

    def find_judge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)
        be_trusted_count = [0] * (n + 1)

        for t in trust:
            a, b = t[0], t[1]
            trust_count[a] += 1
            be_trusted_count[b] += 1

        for t_n, t_c in enumerate(trust_count):
            if t_n == 0:
                continue
            if t_c == 0:
                if be_trusted_count[t_n] == n - 1:
                    return t_n

        return -1


def main():
    solution = SimpleSolution()
    print(solution.find_judge(2, [[1, 2]]))
    # print(9 // 10)
    # print(9 % 10)


if __name__ == "__main__":
    main()
