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


def main():
    solution = SimpleSolution()
    print(solution.max_height_of_triangle(2, 4))


if __name__ == "__main__":
    main()
