from collections import deque
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

        return "".join(find(c) for c in base_str)

    def smallest_equivalent_string_test(self):
        print(self.smallest_equivalent_string("leetcode", "programs", "sourcecode"))

    def robot_with_string(self, s: str) -> str:
        p, t = [], []
        s_list = deque()
        for c in s:
            s_list.append(c)
        while s_list:
            cur = s_list.popleft()
            while t:
                t_last = t[-1]
                if ord(t_last) >= ord(cur):
                    break
                p.append(t.pop())
            t.append(cur)
        while t:
            p.append(t.pop())

        return "".join(p)

    def robot_with_string_test(self):
        print(self.robot_with_string("bdda"))

    def clear_stars(self, s: str) -> str:
        stack = [[] for _ in range(26)]
        for i,c in enumerate(s):
            if c == "*":
                for c_s in stack:
                    if c_s:
                        c_s.pop()
                        break
            else:
                stack[ord(c) - ord("a")].append(i)
        ans = [''] * len(s)
        for index,c_s in enumerate(stack):
            if c_s:
                for i in c_s:
                    ans[i] = chr(index+ord('a'))
        return ''.join(ans)

    def clear_stars_test(self):
        print(self.clear_stars("aaba*"))


def main():
    s = Solution()
    s.clear_stars_test()


if __name__ == "__main__":
    main()
