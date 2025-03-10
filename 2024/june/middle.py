import re
from typing import List


class Solution:

    def discount_price(self, sentence: str, discount: int) -> str:
        """
        le
        """
        word_list = sentence.split(" ")
        price_pattern = r"\$[1-9][0-9]*$"
        for i, word in enumerate(word_list):
            if re.match(price_pattern, word):
                word_num = word[1:]
                if discount == 0:
                    word_num = word_num + ".00"
                elif discount == 100:
                    word_num = "0.00"
                else:
                    discount_result = int(word_num) * (100 - discount) / 100
                    word_num = f"{discount_result:.2f}"
                word_list[i] = "$" + word_num

        return " ".join(word_list)

    def find_lus_length(self, strs: List[str]) -> int:
        """
        这里应该是不需要全排列
        用什么样的数据结构来快速表达
        """
        strs.sort(key=len, reverse=True)
        max_len = len(strs[0])
        repeat_str_list = []
        max_len_list = []
        for cur in strs:
            if cur in repeat_str_list:
                continue

            if len(cur) == max_len:
                if cur in max_len_list:
                    max_len_list.remove(cur)
                    self.find_all_sub_str(repeat_str_list, cur)
                    continue

                max_len_list.append(cur)
                continue

            if len(max_len_list) > 0:
                return max_len

            max_len = len(cur)
            max_len_list.append(cur)

        return -1 if len(max_len_list) == 0 else max_len

    def find_all_sub_str(self, repeat_str_list: List[str], cur: str):
        sub_stack = [cur]
        while len(sub_stack) > 0:
            cur = sub_stack.pop()
            if cur not in repeat_str_list:
                repeat_str_list.append(cur)
                if len(cur) > 1:
                    for i in range(len(cur)):
                        spit_str = cur[:i] + cur[i + 1 :]
                        if spit_str not in sub_stack:
                            sub_stack.append(spit_str)

    def next_greater_elements(self, nums: List[int]) -> List[int]:
        ans = []
        for i, val in enumerate(nums):
            next_greater_val = -1
            loops = 1
            while loops < len(nums):
                next_i = i + loops
                if next_i >= len(nums):
                    next_i = next_i - len(nums)
                if nums[next_i] > val:
                    next_greater_val = nums[next_i]
                    break
                loops += 1
            ans.append(next_greater_val)
        return ans

    def smallest_range(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums)):
            diff = max(nums[-1] - k, nums[i - 1] + k) - min(nums[0] + k, nums[i] - k)
            ans = min(ans, diff)
        return ans


def main():

    solution = Solution()
    print(solution.smallest_range([1, 3, 6], 3))


if __name__ == "__main__":
    main()
