from typing import List


class SimpleSolution:

    def count_beautiful_pairs(self, nums: List[int]) -> int:
        """
        怎么确认两个数互为质数,不过值的范围在[1-9]之间,还是可以枚举的
        """
        beautiful_pair_map = {
            1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [1, 3, 5, 7, 9],
            3: [1, 2, 4, 5, 7, 8],
            4: [1, 3, 5, 7, 9],
            5: [1, 2, 3, 4, 6, 7, 8, 9],
            6: [1, 5, 7],
            7: [1, 2, 3, 4, 5, 6, 8, 9],
            8: [1, 3, 5, 7, 9],
            9: [1, 2, 4, 5, 7, 8],
        }
        count = 0
        for i in range(len(nums) - 1):
            first_digit = int(str(nums[i])[0])
            for j in range(i + 1, len(nums)):
                last_digit = nums[j] % 10
                beautiful_pairs = beautiful_pair_map[first_digit]
                if last_digit in beautiful_pairs:
                    count += 1

        return count

    def temperature_trend(
        self, temperature_a: List[int], temperature_b: List[int]
    ) -> int:
        max_trend_count = 0
        cur_trend_count = 0
        for i in range(len(temperature_a) - 1):
            a_trend = self.cal_temperature_trend(temperature_a[i + 1], temperature_a[i])
            b_trend = self.cal_temperature_trend(temperature_b[i + 1], temperature_b[i])
            if a_trend == b_trend:
                print(f"气温变化趋势相同a_trend={a_trend},i={i}")
                cur_trend_count += 1
            else:
                print(f"气温变化趋势不同a_trend={a_trend},b_trend={b_trend},i={i}")
                max_trend_count = max(max_trend_count, cur_trend_count)
                cur_trend_count = 0
        return max(max_trend_count, cur_trend_count)

    def cal_temperature_trend(
        self, cur_temperature: int, before_temperature: int
    ) -> int:
        if cur_temperature == before_temperature:
            # 平稳
            return 0
        if cur_temperature > before_temperature:
            # 上升
            return 1
        # 下降
        return -1

    def detect_capital_use(self, word: str) -> bool:
        if len(word) == 1:
            return True
        first_char = word[:1]
        remaind_char = word[1:]
        if first_char.isupper():
            if remaind_char.isupper():
                return True
            if remaind_char.islower():
                return True
        else:
            if remaind_char.islower():
                return True

        return False
    
    def smallest_range(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_diff = nums[-1] - nums[0]
        if max_diff <= k * 2:
            return 0
        return max_diff - k * 2


def main():

    solution = SimpleSolution()
    print(
        # solution.temperature_trend(
        #     [-14, 7, -19, 9, 13, 40, 19, 15, -18], [3, 16, 28, 32, 25, 12, 13, -6, 4]
        # ),
        solution.detect_capital_use("USA")
    )


if __name__ == "__main__":
    main()
