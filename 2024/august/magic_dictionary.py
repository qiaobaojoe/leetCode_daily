from typing import List


class MagicDictionary:

    def __init__(self):
        self.len_map = {}

    def build_dict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            d_len = len(d)
            if d_len in self.len_map:
                d_len_list = self.len_map[d_len]
                d_len_list.append(d)
            else:
                self.len_map[d_len] = [d]

    def search(self, search_word: str) -> bool:
        len_search = len(search_word)
        if len_search in self.len_map:
            d_len_list = self.len_map[len_search]
            for cur in d_len_list:
                if self.is_one_diff(search_word, cur):
                    return True
            return False

        else:
            return False

    def is_one_diff(self, search_word: str, target_word: str) -> bool:
        diff_count = 0
        for (i,char_i) in enumerate(search_word):
            if char_i != target_word[i]:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1


def main():
    dic = MagicDictionary()
    dic.build_dict(["hello", "hallo", "leetcode"])
    print(dic.search("hello"))
    print(dic.search("hhllo"))
    


if __name__ == "__main__":
    main()
