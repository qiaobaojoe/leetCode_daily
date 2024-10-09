from typing import List


class SimpleSolution:
    def dest_city(self, paths: List[List[str]]) -> str:
        paths_start =  []
        paths_end = []
        for path in paths:
            paths_start.append(path[0])
            paths_end.append(path[1])
        for start in paths_start:
            if start in paths_end:
                paths_end.remove(start)
        return paths_end[0]

def main():
    solution = SimpleSolution()
    print(solution.dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

if __name__ == '__main__':
    main()