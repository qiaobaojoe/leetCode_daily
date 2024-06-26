from typing import List


class GraphAdjacencyMatrix:
    """
    邻接矩阵表示图
    """

    def __init__(self, vertices: List[int], edges: List[List[int]]) -> None:
        self.vertices: List[int] = []
        self.adj_mat: List[List[int]] = []
        # 添加顶点
        for v in vertices:
            self.add_vertex(v)
        # 添加边
        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self) -> int:
        return len(self.vertices)

    def add_vertex(self, val: int):
        n = self.size()
        self.vertices.append(val)
        new_row = [0] * n
        self.adj_mat.append(new_row)
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self, index: int):
        if index >= self.size():
            raise IndexError()
        self.vertices.pop(index)
        self.adj_mat.pop(index)
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    def print(self):
        """打印邻接矩阵"""
        print("顶点列表 =", self.vertices)
        print("邻接矩阵 =")
        for row in self.adj_mat:
            for element in row:
                print(element, end=" ")
            print()


def main():
    graph_adj = GraphAdjacencyMatrix(
        [1, 3, 2, 5, 4], [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    )
    graph_adj.print()
    graph_adj.remove_vertex(1)
    graph_adj.print()


if __name__ == "__main__":
    main()
