from typing import List


class SimpleSolution:
    def dest_city(self, paths: List[List[str]]) -> str:
        paths_start = []
        paths_end = []
        for path in paths:
            paths_start.append(path[0])
            paths_end.append(path[1])
        for start in paths_start:
            if start in paths_end:
                paths_end.remove(start)
        return paths_end[0]

    def number_of_pairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for n1 in nums1:
            for n2 in nums2:
                if n1 % (n2 * k) == 0:
                    ans += 1
        return ans

    def max_height_of_triangle(self, red: int, blue: int) -> int:
        first, second, red_ans = red, blue, 1
        while True:
            if red_ans % 2 == 1:
                first -= red_ans
                if first < 0:
                    red_ans -= 1
                    break
                red_ans += 1
            else:
                second -= red_ans
                if second < 0:
                    red_ans -= 1
                    break
                red_ans += 1

        first, second, blue_ans = blue, red, 1
        while True:
            if blue_ans % 2 == 1:
                first -= blue_ans
                if first < 0:
                    blue_ans -= 1
                    break
                blue_ans += 1
            else:
                second -= blue_ans
                if second < 0:
                    blue_ans -= 1
                    break
                blue_ans += 1

        return max(red_ans, blue_ans)

    def count_complete_day_pairs(self, hours: List[int]) -> int:

        ans = 0
        for i in range(len(hours) - 1):
            hour_i = hours[i]
            for j in range(i + 1, len(hours)):
                hour_j = hours[j]
                if (hour_i + hour_j) % 24 == 0:
                    ans += 1
        return ans

    def get_smallest_string(self, s: str) -> str:
        ans = s
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                parity_i = int(s[i]) % 2
                parity_j = int(s[i + 1]) % 2
                if parity_i == parity_j:
                    ans = s[:i] + s[i + 1] + s[i] + s[i + 2 :]
                    break
        return ans


def main():
    solution = SimpleSolution()
    print(solution.get_smallest_string("45320"))


if __name__ == "__main__":
    main()
