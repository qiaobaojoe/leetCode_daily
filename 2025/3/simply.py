from typing import List


class Solution:
    def count_prefixes(self, words: List[str], s: str) -> int:
        ans = 0
        prefix_word = []
        for i in range(len(s)):
            prefix_word.append(s[: i + 1])
        print(prefix_word)
        for word in words:
            if len(word) > len(s):
                continue
            if word == prefix_word[len(word) - 1]:
                ans += 1
        return ans

    def minimum_sum(self, n: int, k: int) -> int:
        ans_array = []
        cursor = 1
        while len(ans_array) < n:
            if cursor >= k:
                ans_array.append(cursor)
                cursor += 1
                continue
            if (k - cursor) not in ans_array:
                ans_array.append(cursor)
            cursor += 1
        return sum(ans_array)

    def minimum_cost(self, s: str) -> int:
        cost = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                continue
            # 字符不同，开始反转
            cost += min(i + 1, len(s) - i - 1)
        return cost

    def can_be_valid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        mn,mx = 0, 0
        for b, lock in zip(s, locked):
            if lock == '1':  # 不能改
                d = 1 if b == '(' else -1
                mx += d
                if mx < 0:  # c 不能为负
                    return False
                mn += d
            else:  # 可以改
                mx += 1  # 改成左括号，c 加一
                mn -= 1  # 改成右括号，c 减一
            if mn < 0:  # c 不能为负
                mn = 1  # 此时 c 的取值范围都是奇数，最小的奇数是 1
        return mn == 0  # 说明最终 c 能是 0


def main():
    s = Solution()
    print(s.can_be_valid("(((())", "111111"))


if __name__ == "__main__":
    main()
