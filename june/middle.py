import re


class Solution:

    def discount_price(self, sentence: str, discount: int) -> str:
        word_list = sentence.split(" ")
        price_pattern = r"\$[1-9][0-9]*$"
        for i, word in enumerate(word_list):
            if re.match(price_pattern, word):
                word_num = word[1:]
                if discount == 0:
                    word_num = word_num + ".00"
                elif discount == 100:
                    word_num = "0.00"
                else:
                    discount_result = int(word_num) * (100 - discount) / 100
                    word_num = f"{discount_result:.2f}"
                word_list[i] = "$" + word_num

        return " ".join(word_list)


def main():

    solution = Solution()
    print(solution.discount_price("ka3caz4837h6ada4 r1 $602", 9))


if __name__ == "__main__":
    main()
