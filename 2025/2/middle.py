from typing import List


# 这个类是2月份中等难度leetcode算法的实现
class Solution:
    def max_distance(self, arrays: List[List[int]]) -> int:
        # 暴力解法，遍历所有可能的组合，计算距离
        m = len(arrays)
        ans_arrays = [[] for _ in range(m)]
        for i, nums in enumerate(arrays):
            ans_arrays[i].append(nums[0])
            ans_arrays[i].append(nums[-1])
        ans = 0
        for i, a in enumerate(ans_arrays):
            for j in range(m):
                if i == j:
                    continue
                ans = max(ans, abs(a[0] - ans_arrays[j][1]))
        return ans


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def change_rating(self, food: str, new_rating: int) -> None:
        for i, f in enumerate(self.foods):
            if f == food:
                self.ratings[i] = new_rating
                return

    def highest_rated(self, cuisine: str) -> str:
        ans_c = []
        for i, c in enumerate(self.cuisines):
            if c == cuisine:
                ans_c.append(i)
        if not ans_c:
            return ""
        max_rating = 0
        ans = ""
        for i in ans_c:
            if self.ratings[i] > max_rating:
                max_rating = self.ratings[i]
                ans = self.foods[i]
            if self.ratings[i] == max_rating:
                if self.foods[i] < ans:
                    ans = self.foods[i]
        return ans


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


# 主程序入口
if __name__ == "__main__":
    food = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
    )
