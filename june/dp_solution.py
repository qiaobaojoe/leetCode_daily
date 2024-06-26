from typing import List


class DpSolution:
    """
    动态规划相关的题目合集
    动态方程的目的就是剪枝,我可以通过其他暴力的方式去完成解决问题
    现在的我对于动态规划的理解不好,使用起来也不熟练,就按照自己的理解通过暴力的方式去做
    """

    def max_score(self, nums: List[int], x: int) -> int:
        """
        https://leetcode.cn/problems/visit-array-positions-to-maximize-score/description/?envType=daily-question&envId=2024-06-14
        那么你可以移动到满足 i < j 的 任意 位置 j 。 只能往前走
        nums[i] 和 nums[j] 的 奇偶性 不同，那么你将失去分数 x 我当前的选择会影响下一步 如果没有这个条件把所有值都加在一起就行了
        一开始 在数组的位置 0 处 遍历的起始位置是确定的

        1.数组内所有元素的奇偶性一样,全部加载一起就行了
        2.暴力的解法,遍历所有可能得组合
        """
        ans = nums[0]
        #可以选择的

        return ans

    def is_even_numver(self, num: int) -> bool:
        """
        是否为偶数
        true 偶数/false 奇数
        """
        return num % 2 == 0


def main():
    solution = DpSolution()
    print(solution.max_score([2, 3, 6, 1, 9, 2], 5))
    print(solution.max_score([2, 4, 6, 8], 3))


if __name__ == "__main__":
    main()
