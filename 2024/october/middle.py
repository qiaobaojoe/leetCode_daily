class MiddleSolution:

    def nth_person_gets_nth_seat(self, n: int) -> float:
        # 其实只要想一下，n个座一共会有2^(n-1)种可能，然后最后一个座不被占的话，就是当最后一个座不存在，
        # 前面随便他们怎么坐，所以其实就相当于n-1个座一共有多少种情况，也就是2^(n-2)种，所以可能性就是0.5了，
        # 但是n-2>=0，所以1得单拿出来讨论
        if n == 1:
            return 1.0
        return 0.5


def main():
    solution = MiddleSolution()
    print(solution.nth_person_gets_nth_seat(1))


if __name__ == "__main__":
    main()
