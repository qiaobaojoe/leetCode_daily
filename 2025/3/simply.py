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


def main():
    s = Solution()
    print(s.minimum_cost("0011"))
    print(s.minimum_cost("010101"))


if __name__ == "__main__":
    main()
