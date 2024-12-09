class MiddleSolution:
    def knight_probability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        step_plan_count = 8 ** k
        step_out_plan_count = 0
        step_plan = [(row, column)]
        while k > 0:
            cur_step_plan = step_plan[::]
            step_plan = []
            k -= 1
            while cur_step_plan:
                (i, j) = cur_step_plan.pop()
                # 每一步有8个方向可以走
                # 上2
                if i - 2 >= 0 and j - 1 >= 0:
                    step_plan.append((i - 2, j - 1))
                else:
                    step_out_plan_count += 8 ** k
                if i - 2 >= 0 and j + 1 < n:
                    step_plan.append((i - 2, j + 1))
                else:
                    step_out_plan_count += 8 ** k
                # 上1
                if i - 1 >= 0 and j - 2 >= 0:
                    step_plan.append((i - 1, j - 2))
                else:
                    step_out_plan_count += 8 ** k
                if i - 1 >= 0 and j + 2 < n:
                    step_plan.append((i - 1, j + 2))
                else:
                    step_out_plan_count += 8 ** k
                # 下2
                if i + 2 < n and j - 1 >= 0:
                    step_plan.append((i + 2, j - 1))
                else:
                    step_out_plan_count += 8 ** k
                if i + 2 < n and j + 1 < n:
                    step_plan.append((i + 2, j + 1))
                else:
                    step_out_plan_count += 8 ** k
                # 下1
                if i + 1 < n and j - 2 >= 0:
                    step_plan.append((i + 1, j - 2))
                else:
                    step_out_plan_count += 8 ** k
                if i + 1 < n and j + 2 < n:
                    step_plan.append((i + 1, j + 2))
                else:
                    step_out_plan_count += 8 ** k
            
        if step_plan_count == 0:
            return 0
        return 1 - step_out_plan_count / step_plan_count


def main():
    solution = MiddleSolution()
    print(solution.knight_probability(8, 30, 6, 4))


if __name__ == "__main__":
    main()
