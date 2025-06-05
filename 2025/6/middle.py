from string import ascii_lowercase


class Solution:
    def smallest_equivalent_string(self, s1: str, s2: str, base_str: str) -> str:
        fa = {c: c for c in ascii_lowercase}

        def find(x: str) -> str:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def merge(x: str, y: str) -> None:
            small, big = sorted((find(x), find(y)))
            fa[big] = small  # 把大的代表元指向小的代表元

        for x, y in zip(s1, s2):
            merge(x, y)

        return ''.join(find(c) for c in base_str)


    def smallest_equivalent_string_test(self):
        print(self.smallest_equivalent_string("leetcode", "programs", "sourcecode"))


def main():
    s = Solution()
    s.smallest_equivalent_string_test()


if __name__ == "__main__":
    main()
