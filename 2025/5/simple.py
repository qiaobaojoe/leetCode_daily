from typing import List


class SimpleSolution:
    def build_array(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans

    def find_even_numbers(self, digits: List[int]) -> List[int]:
        ans = []
        even_flag = []
        for d in digits:
            even_flag.append(d % 2)
        if sum(even_flag) == len(digits):
            return ans

        for i, d in enumerate(digits):
            if d == 0:
                # 数字不含前导零
                continue
            for j, e in enumerate(digits):
                if i == j:
                    continue
                for k, f in enumerate(digits):
                    if i == k or j == k:
                        continue
                    if even_flag[k]:
                        continue
                    num = d * 100 + e * 10 + f
                    if ans.count(num) > 0:
                        continue
                    ans.append()
        ans.sort()
        return ans

    def three_consecutive_odds(self, arr: List[int]) -> bool:
        for i, a in enumerate(arr):
            arr[i] = a % 2
        j = 0
        while j < len(arr) - 2:
            if arr[j] == 0:
                j += 1
                continue
            odd_len = 1
            while odd_len < 3:
                j += 1
                if arr[j] == 1:
                    odd_len += 1
                else:
                    break
            if odd_len == 3:
                return True
        return False

    def get_longest_subsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        before_i= 0

        for i in range(1, len(groups)):
            if groups[i] != groups[before_i]:
                before_i = i
                ans.append(words[i])
        return ans


def main():
    s = SimpleSolution()
    # print(s.get_longest_subsequence(["d"], [1]))
    print(s.get_longest_subsequence(["e", "a", "b"], [0, 0, 1]))


if __name__ == "__main__":
    main()
