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
                    num = d * 100 +  e * 10 +f
                    if ans.count(num) > 0:
                        continue
                    ans.append()
        ans.sort()
        return ans


def main():
    s = SimpleSolution()
    # print(s.find_even_numbers([3, 7, 5]))
    print(s.find_even_numbers([2, 1, 3, 0]))


if __name__ == "__main__":
    main()
