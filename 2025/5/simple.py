from typing import List

class SimpleSolution:
    def build_array(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans


def main():
    s = SimpleSolution()
    print(s.build_array([0,2,1,5,3,4]))


if __name__ == "__main__":
    main()
