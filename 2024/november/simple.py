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


def main():
    solution = Simplesolution()
    print(solution.min_changes(13, 4))


if __name__ == "__main__":
    main()
