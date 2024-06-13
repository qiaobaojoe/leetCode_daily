from collections import deque
from typing import List, Optional
from tree import TreeNode


class BinarySearchTree:
    def __init__(self):
        self._root: Optional[TreeNode] = None

    # 验证过了，没有问题
    def search(self, val: int) -> Optional[TreeNode]:
        if self._root is None:
            return None
        root_node = self._root
        while root_node:
            root_val = root_node.val
            if root_val == val:
                return root_node
            if root_val > val:
                root_node = root_node.left
            if root_val < val:
                root_node = root_node.right
        return None

    def insert(self, val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not self._root:
            self._root = new_node
            return new_node

        root_node = self._root
        pre_node = root_node
        while root_node:
            root_val = root_node.val
            if root_val == val:
                print("重复数据,无法插入")
                return None
            pre_node = root_node
            if root_val > val:
                root_node = root_node.left
            else:
                root_node = root_node.right

        if pre_node.val > val:
            pre_node.left = new_node
        else:
            pre_node.right = new_node
        return self._root

    def remove(self, val: int) -> Optional[TreeNode]:
        # 删除是最为复杂的,首先要找到节点,再根据子节点的数量分别处理

        pass

    def asc_order_list(self) -> List[int]:
        "中序遍历"
        pass

    def level_order_list(self) -> List[List[int]]:
        "层序遍历"
        ans = []
        if not self._root:
            return ans
        node_list = deque()
        node_list.append(self._root)
        while len(node_list) > 0:
            cur_ans = []
            for _ in range(len(node_list)):
                cur = node_list.popleft()
                cur_ans.append(cur.val)
                if cur.left:
                    node_list.append(cur.left)
                if cur.right:
                    node_list.append(cur.right)
            ans.append(cur_ans)
        return ans


class Solution:
    def main():
        search_tree = BinarySearchTree()
        search_tree.insert(8)
        search_tree.insert(12)
        search_tree.insert(4)
        search_tree.insert(6)
        search_tree.insert(2)
        search_tree.insert(10)
        search_tree.insert(14)
        search_tree.insert(1)
        search_tree.insert(3)
        search_tree.insert(5)
        search_tree.insert(7)
        search_tree.insert(11)
        search_tree.insert(9)
        search_tree.insert(15)
        search_tree.insert(13)
        print(f"层序遍历={search_tree.level_order_list()}")

    if __name__ == "__main__":
        main()
