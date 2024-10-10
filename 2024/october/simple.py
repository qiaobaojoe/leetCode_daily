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


def main():
    solution = SimpleSolution()
    print(solution.number_of_pairs([1, 2, 3, 4], [1, 2, 3, 4], 3))


if __name__ == "__main__":
    main()
