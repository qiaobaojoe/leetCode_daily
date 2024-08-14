from typing import List


class Soluton:

    def is_array_special(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # 判断是否特殊数组的方法是现成的，最简单的方法就是遍历每个子数组区间，优化的空间我认为就是去除重复的查询区间，判断的方法是没有办法简化的了
        # 居然是动态规划，我一直都很害怕，因为我理解不了
        # 对于我太难了，就先从模仿理解开始，不要想着一次全部弄明白
        # 前缀和算法，新的知识
        n = len(nums)
        presum = [0] * n
        for i in range(1, n):
            if (nums[i] + nums[i - 1]) % 2 == 1:
                presum[i] = presum[i - 1] + 1
            else:
                presum[i] = presum[i - 1]
        ans = []
        for from_, to in queries:
            if (to - from_) == (presum[to] - presum[from_]):
                ans.append(True)
            else:
                ans.append(False)
        return ans


def main():
    solution = Soluton()
    print(solution.is_array_special([3, 4, 1, 2, 6], [[0, 4]]))


if __name__ == "__main__":
    main()
