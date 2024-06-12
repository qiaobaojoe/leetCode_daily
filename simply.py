from typing import List


class Solution:
    def distanceTraveled(self, mainTank: int, additionTank: int) -> int:
        dis = 0
        while mainTank > 0:
            if mainTank >= 5:
                dis += 5 * 10
                mainTank -= 5
                if additionTank > 0:
                    additionTank -= 1
                    mainTank += 1
                continue
            else:
                dis += mainTank * 10
                mainTank = 0
        return dis

    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        num = 0
        for hour in hours:
            if hour >= target:
                num += 1
        return num

    def makeFancyString(self, s: str) -> str:
        same_char = 0
        cur = ""
        result = []
        for char in s:
            if cur == "":
                cur = char
                same_char = 1
                result.append(char)
            else:
                if char == cur:
                    if same_char == 2:
                        # 超出限制，当前字符要去除
                        continue
                    else:
                        result.append(char)
                        same_char += 1
                        continue
                else:
                    cur = char
                    same_char = 1
                    result.append(char)
                    continue

        return "".join(result)

    def makeFancyStringOptimize(self, s: str) -> str:
        count = 1
        result = []
        result.append(s[0])
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                result.append(s[i])

        return "".join(result)

    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count_tested = 0
        for device in batteryPercentages:
            if (device - count_tested) > 0:
                count_tested += 1
        return count_tested

    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t

    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        # 峰值 严格的大于相邻的元素。通过一下遍历获取结果，我想到双指针
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                ans.append(i)
        return ans

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        dis_index = 0
        dis_num = 1

        while candies > 0:
            print(
                f"dis_index={dis_index},dis_num={dis_num},candies={candies},ans={ans}"
            )
            if candies >= dis_num:
                ans[dis_index] += dis_num
                candies -= dis_num
            else:
                ans[dis_index] += candies
                candies = 0
                break

            dis_num += 1
            dis_index += 1
            dis_index = dis_index % num_people
        return ans

    def minimumSteps(self, s: str) -> int:
        step = 0
        black_idx = []
        for inx, val in enumerate(s):
            if "1" == val:
                black_idx.append(inx)

        if len(black_idx) == 0:
            return step
        right_pos = len(s) - 1
        for inx in black_idx[::-1]:
            step += right_pos - inx
            right_pos -= 1

        return step

    def maxOperations(self, nums: List[int]) -> int:
        times = 1
        score = nums[0] + nums[1]
        while times * 2 + 2 <= len(nums):
            if score == (nums[times * 2] + nums[times * 2 + 1]):
                times += 1
            else:
                break
        return times
    
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        remand = purchaseAmount % 10 
        time = purchaseAmount // 10
        if remand >= 5 :
            time += 1 
        return 100 - 10 * time


if __name__ == "__main__":
    solution = Solution()
    dis = solution.maxOperations([1,1,1,1,1,1])
    print(dis)
