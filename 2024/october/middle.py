from typing import List


class MiddleSolution:

    def max_energy_boost(self, energy_drink_a: List[int], energy_drink_b: List[int]) -> int:
        a,b = energy_drink_a,energy_drink_b
        n = len(a)
        dp = [[0,0] for _ in range(n+1) ]

        for i in range(1,n+1):
            if i == 1:
                dp[1][0] = a[0]
                dp[1][1] = b[0]
            elif i == 2:
                dp[2][0] = max(dp[1][0] + a[1],dp[1][1])
                dp[2][1] = max(dp[1][1] + b[1],dp[1][0])
            else:
                dp[i][0] = max(dp[i-1][0] + a[i-1],dp[i-2][1] + a[i-1])
                dp[i][1] = max(dp[i-1][1] + b[i-1],dp[i-2][0] + b[i-1])

        return max(dp[n][1],dp[n][0])


def main():
    solution = MiddleSolution()
    print(solution.max_energy_boost([4,1,1],[1,1,3]))


if __name__ == "__main__":
    main()
