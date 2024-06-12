from bisect import bisect_right
from collections import Counter, defaultdict
from typing import List


class SnapshotArray:

    def __init__(self, length: int) -> None:
        self.array = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        index_array = self.array[index]
        if len(index_array) == 0:
            return 0
        if snap_id < 0:
            return 0
        right = SnapshotArray.bisect_right([a for (a, b) in index_array], snap_id)
        return index_array[right][1] if right > -1 else 0

    # 给一个有序数组，但是包含重复数据。传入目标值，如果存在找到最右侧的索引，不存在，找到比它小的最接近值的最右侧索引
    def searchRight(snap_arry, target: int) -> int:

        bisect_right()
        print(snap_arry, target)
        l = 0
        r = len(snap_arry) - 1
        if snap_arry[l] > target:
            return -1
        if snap_arry[r] < target:
            return snap_arry[r]

        result = -1
        while l < r:
            print("二分查找迭代 l={},r = {}".format(l, r))
            m = (l + r) // 2
            if snap_arry[m] == target:
                result = m
                l = m + 1
                continue
            if snap_arry[m] < target:
                l = m + 1
                continue
            if snap_arry[m] > target:
                r = m - 1
                continue

        print("退出 l={},r = {}".format(l, r))
        if snap_arry[max(l, r)] == target:
            return max(l, r)

        if result != -1:
            return result
        else:
            if snap_arry[min(l, r)] > target:
                return min(l, r) - 1
            else:
                return min(l, r)

    # Your SnapshotArray object will be instantiated and called as such:
    # obj = SnapshotArray(length)
    # obj.set(index,val)
    # param_2 = obj.snap()
    # param_3 = obj.get(index,snap_id)


class Solution:

    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        result = []
        while n != 0:
            print("进入循环 n = {}".format(n))
            remainder = n % -2
            print("进入循环 remainder = {}".format(remainder))
            result.append(str(abs(remainder)))
            if remainder < 0:
                n = n // -2 + 1
            else:
                n = n // -2
        print("退出循环 n = {}".format(n))

        return "".join(result[::-1])

    def base2(self, n: int) -> str:
        if n == 0:
            return "0"

        result = ""
        while n // 2 != 0:
            remainder = n % 2
            result = result + str(remainder)
            n = n // 2

        result = result + str(1)

        return result[::-1]

    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            print(xor_sum)

        print(bin(xor_sum))
        lsb = xor_sum & (-xor_sum)
        num1 = num2 = 0
        for num in nums:
            if lsb & num:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]

    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step_sum = 0
        watering_index = 0
        cur_capacity = capacity
        plants_len = len(plants)
        while watering_index < plants_len:
            for index in range(watering_index, plants_len):
                if cur_capacity >= plants[index]:
                    cur_capacity -= plants[index]
                    watering_index += 1
                    step_sum += 1
                else:
                    print("水不够浇灌，重新走回打水")
                    cur_capacity = capacity
                    step_sum += 2 * watering_index
                    break
        return step_sum

    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        # 双端队列，每次步进一
        refill_sum = 0
        a_index = 0
        b_index = len(plants) - 1
        a_cur_cap = capacityA
        b_cur_cap = capacityB
        while a_index < b_index:
            if plants[a_index] > a_cur_cap:
                refill_sum += 1
                a_cur_cap = capacityA
            a_cur_cap -= plants[a_index]
            a_index += 1

            if plants[b_index] > b_cur_cap:
                refill_sum += 1
                b_cur_cap = capacityB
            b_cur_cap -= plants[b_index]
            b_index -= 1

        if a_index == b_index:
            if b_cur_cap > a_cur_cap:
                if plants[b_index] > b_cur_cap:
                    refill_sum += 1
            else:
                if plants[a_index] > a_cur_cap:
                    refill_sum += 1

        return refill_sum

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        return (
            self.garbage_type_sum(garbage, travel, "M")
            + self.garbage_type_sum(garbage, travel, "P")
            + self.garbage_type_sum(garbage, travel, "G")
        )

    def garbage_type_sum(
        self, garbage: List[str], travel: List[int], garbage_type: str
    ) -> int:
        time_sum = 0
        travel_index = 0
        for index, garbage_type_list in enumerate(garbage):
            count = garbage_type_list.count(garbage_type)
            if count > 0:
                time_sum += count
                travel_index = index

        time_sum += sum(travel[:travel_index])
        print("garbage_type = {}, time_sum ={}".format(garbage_type, time_sum))
        return time_sum

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 深度优先算法，用一个列表记录下来所有分叉
        # 确定下来图的边间
        M = len(grid)
        N = len(grid[0])
        # 腐败橘子的坐标（x,y）
        queue = []
        # 新鲜橘子的数量
        count = 0

        for x in range(N):
            for y in range(M):
                if grid[y][x] == 1:
                    count += 1
                if grid[y][x] == 2:
                    queue.append((x, y))

        round = 0
        while count > 0 and len(queue) > 0:
            round += 1
            for i in range(len(queue)):
                # 上
                (x, y) = queue.pop(0)
                if y - 1 >= 0 and grid[y - 1][x] == 1:
                    grid[y - 1][x] = 2
                    count -= 1
                    queue.append((x, y - 1))
                # 下
                if y + 1 < M and grid[y + 1][x] == 1:
                    grid[y + 1][x] = 2
                    count -= 1
                    queue.append((x, y + 1))
                # 左
                if x - 1 >= 0 and grid[y][x - 1] == 1:
                    grid[y][x - 1] = 2
                    count -= 1
                    queue.append((x - 1, y))
                # 右
                if x + 1 < N and grid[y][x + 1] == 1:
                    grid[y][x + 1] = 2
                    count -= 1
                    queue.append((x + 1, y))

        if count > 0:
            return -1
        else:
            return round

    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # 不是动态规划，每个工人的收益是独立的，不会互相影响
        # 有一极其巧妙地优化方式，先对worker进行牌，后续寻找最大工作量只需要遍历一次
        my_tuple = []
        for index, diff in enumerate(difficulty):
            my_tuple.append((diff, profit[index]))
        print(my_tuple)
        sorted_tuple = sorted(my_tuple, key=lambda x: x[0])
        print(sorted_tuple)

        sum_profit = 0
        diff_index = 0
        max_profit = 0
        worker.sort()
        print(worker)
        for w in worker:

            for cur in range(diff_index, len(sorted_tuple)):
                print(cur)
                (d, f) = sorted_tuple[cur]
                if w >= d:
                    max_profit = max(max_profit, f)
                    diff_index = cur
                    print(diff_index, max_profit)
                else:
                    break
            sum_profit += max_profit

        return sum_profit

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        no_lose = []
        one_lose = []

        lose_counter = Counter()
        for winner, loser in matches:
            if winner not in lose_counter:
                lose_counter[winner] = 0
            lose_counter[loser] += 1
        for key, value in lose_counter.items():
            if value == 0:
                no_lose.append(key)
            if value == 1:
                one_lose.append(key)
        no_lose.sort()
        one_lose.sort()

        return [no_lose, one_lose]

    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_map = defaultdict(list)
        for i, num in enumerate(nums):
            pos_map[num].append(i)

        longest = 0
        for pos_list in pos_map.values():
            longest = max(self.cur_equal_subarray(pos_list, k), longest)

        return longest

    def cur_equal_subarray(self, pos_list: List[int], k: int) -> int:
        pos_size = len(pos_list)
        if (pos_list[pos_size - 1] - pos_list[0]) + 1 - pos_size <= k:
            return pos_size

        cur_longest = 0
        window_size = 0  # 窗口大小定义在外面,不用每一次都重新寻找窗口大小，这一步很重要
        for i in range(len(pos_list)):
            while (
                i + window_size + 1 < len(pos_list)
                and pos_list[i + window_size + 1] - pos_list[i] - window_size - 1 <= k
            ):
                window_size += 1

            cur_longest = max(cur_longest, window_size + 1)

        return cur_longest

    def mostCompetitive_exhaustion(self, nums: List[int], k: int) -> List[int]:

        sub_array_list = self.all_sub_array(nums, k)
        # 得到所有的子序列尝试,遍历比较得到结果
        for i in range(k):
            cur_min = None
            for sub in sub_array_list:
                if cur_min is None:
                    cur_min = sub[i]
                else:
                    cur_min = min(cur_min, sub[i])

            copy_list = sub_array_list[:]
            for sub in sub_array_list:
                if sub[i] > cur_min:
                    copy_list.remove(sub)
            sub_array_list = copy_list

        return sub_array_list[0]

    def all_sub_array(self, nums: List[int], k: int) -> List[List[int]]:
        sub_array_list = [nums]
        if k == len(nums):
            sub_array_list.append(nums)
            return sub_array_list
        while k < len(nums):
            print(k)
            wait_sub_array = sub_array_list[:]
            sub_array_list = []

            for w in wait_sub_array:
                for i in w:
                    new_w = w[:]
                    new_w.remove(i)
                    sub_array_list.append(new_w)
            k += 1

        return sub_array_list

    def mostCompetitive2(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i, x in enumerate(nums):
            while len(res) > 0 and len(nums) - i + len(res) > k and res[-1] > x:
                res.pop()
            res.append(x)
            print(f"res = {res},i= {i}")
        return res[:k]

    def mostCompetitive3(self, nums: List[int], k: int) -> List[int]:
        # 对上面方法进行剪枝,第一个不相同的数组,越小就越好.
        # 所以为题就是找到可以裁剪出子序列范围内，最小的值
        ans = []
        help_list = nums[::1]
        for i in range(k, 0, -1):
            sub_index = self.most_competitive_support(help_list, i)
            ans.append(help_list[sub_index])
            help_list = help_list[sub_index + 1 : :]
        return ans

    def most_competitive_support(self, nums: List[int], k: int) -> int:
        # 对上面方法进行剪枝,第一个不相同的数组,越小就越好.
        # 所以为题就是找到可以裁剪出子序列范围内，最小的值
        help_list = nums[0 : len(nums) - k + 1 : 1]
        min_value = min(help_list)
        return nums.index(min_value)

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # 先判断是否可行
        missing_rolls = []
        m = len(rolls)
        diff = (m + n) * mean - sum(rolls)
        if diff > n * 6 or diff < n:
            print("不可能")
            return missing_rolls
        div = diff // n
        remainder = diff % n
        for i in range(n):
            if remainder > 0:
                missing_rolls.append(div + 1)
                remainder -= 1
            else:
                missing_rolls.append(div)
        return missing_rolls

    def maximumLength(self, s: str) -> int:
        # 暴力构建所有的子字符串，放在hashMap中统计结果
        sub_str_counter = Counter()
        s_len = len(s)
        for i in range(1, s_len + 1):
            for k in range(s_len - i + 1):
                cur_sub = s[k : k + i]
                char_set = set(cur_sub)
                if len(char_set) == 1:
                    sub_str_counter[cur_sub] += 1
        sorted_sub = sub_str_counter.most_common()
        ans = -1
        for sub, count in sorted_sub:
            if count < 3:
                break
            ans = max(ans, len(sub))

        return ans

    def maximumLengthV2(self, s: str) -> int:
        # 哈哈，一切都是如此的巧妙，昨天没有改进暴力解法的版本，今天的题目就是改进。暴力解法会超时
        # 二分查找的方法我理解不了
        # 统计每个字符的连续最大长度  连续长度为 n 可以拆分成(k+1)个n-k长度的子串
        char_set = set(s)
        char_length = {char: [] for char in char_set}

        cur_l = 1
        len_s = len(s)
        for i, char in enumerate(s):
            if i < len_s -1 :
                if char != s[i+1]:
                    char_length[char].append(cur_l)
                    cur_l = 1
                else:
                    cur_l +=1
            else :
                # 最后一个字符的判断
                if char != s[i-1]:
                    # char_length[s[i-1]].append(cur_l)
                    char_length[char].append(1)
                else:
                    char_length[char].append(cur_l)

        print(char_length)
        ans = -1
        for char, len_list in char_length.items():
            len_list_copy = len_list[::]
            l_max = max(len_list_copy)
            while l_max > 1:
                len_count = len_list_copy.count(l_max)
                if len_count >= 3:
                    ans = max(ans, l_max)
                    break
                else:
                    print("拆分最长数组")
                    for _ in range(len_count):
                        len_list_copy.remove(l_max)
                        len_list_copy.append(l_max - 1) 
                        len_list_copy.append(l_max - 1) 
                    print(len_list_copy)
                    l_max -= 1


            if len(len_list_copy) >= 3:
                ans = max(ans, 1)
        return ans
    
    def countBattleships(self, border: List[List[str]]) -> int:
        ship_direction = []
        x_m = len(border)
        y_n = len(border[0])
        for y, x_list in enumerate(border):
            for x, cur in enumerate(x_list):
                if "X" == cur:
                    ship_direction.append((x, y))
        ship_count = 0
        print(f"ship_direction ={ship_direction}")
        while len(ship_direction) > 0:
            x, y = ship_direction.pop()
            print(f"x ={x},y={y}")
            ship_count += 1
            around = []
            self.set_around(x, y, around, x_m, y_n)

            while len(around) > 0:
                around_c = around[::]
                for ax, ay in around_c:
                    print(f"ax ={ax},ay={ay}")
                    around.remove((ax, ay))
                    if ship_direction.count((ax, ay)) > 0:
                        ship_direction.remove((ax, ay))
                        self.set_around(ax, ay, around, x_m, y_n)

        return ship_count

    def set_around(self, x: int, y: int, around: List[int], x_m: int, y_n: int) -> None:
        # 左
        if x != 0:
            around.append((x - 1, y))
        # 右
        if x != y_n - 1:
            around.append((x + 1, y))
        # 上
        if y != 0:
            around.append((x, y - 1))
        # 下
        if y != x_m - 1:
            around.append((x, y + 1))

    def countBattleships_2(self, border: List[List[str]]) -> int:
        # 本来是不想重写官方的答案，但是他的解法实在太巧妙了。
        # 遍历数组是有顺序的 左->右,上->下 当前为X，如果左边和上面都不是X则表明这是一个新的战舰
        ans = 0
        for y, x_list in enumerate(border):

            for x, cur in enumerate(x_list):
                if "X" == cur:
                    if (x == 0 or border[y][x - 1] != "X") and (
                        y == 0 or border[y - 1][x] != "X"
                        ):
                        ans += 1
        return ans


def main():

    solution = Solution()
    # print(solution.maximumLength("cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"))
    # print(solution.maximumLengthV2("cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"))
    print(solution.maximumLengthV2("bbc"))


if __name__ == "__main__":
    main()
