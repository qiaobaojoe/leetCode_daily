from typing import List


class Traceback:

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.combination_sum_trace([], target, candidates, 0, ans)
        return ans

    def combination_sum_trace(
        self,
        state: List[int],
        target: int,
        choices: List[int],
        start: int,
        ans: List[List[int]],
    ):
        if 0 == target:
            ans.append(state[::])
            return

        for i in range(start, len(choices)):
            choice = choices[i]
            if target - choice >= 0:
                state.append(choice)
                self.combination_sum_trace(state, target - choice, choices, i, ans)
                state.pop()
            else:
                break

    def combination_sum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.combination_sum_trace_2([], target, candidates, 0, ans)
        return ans

    def combination_sum_trace_2(
        self,
        state: List[int],
        target: int,
        choices: List[int],
        start: int,
        ans: List[List[int]],
    ):
        if 0 == target:
            ans.append(state[::])
            return

        for i in range(start, len(choices)):
            choice = choices[i]
            if i > start and choice == choices[i - 1]:
                continue
            if target - choice >= 0:
                state.append(choice)
                self.combination_sum_trace_2(
                    state, target - choice, choices, i + 1, ans
                )
                state.pop()
            else:
                break


def main():
    trackback = Traceback()
    print(trackback.combination_sum([2, 3, 6, 7], 7))
    print(trackback.combination_sum_2([2, 5, 2, 1, 2], 5))


if __name__ == "__main__":
    main()
