from collections import deque
from typing import List, Optional
from tree import TreeNode


class BinarySearchTree:
    
    def __init__(self):
        self._root: Optional[TreeNode] = None

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
        if not self._root:
            return self._root

        # 删除是最为复杂的,首先要找到节点,再根据子节点的数量分别处理
        search_node = self._root
        pre_node = None

        while search_node:
            search_val = search_node.val
            if search_val == val:
                break
            pre_node = search_node
            if search_val > val:
                search_node = search_node.left
            if search_val < val:
                search_node = search_node.right
        if not search_node:
            print("没有找到,无需删除")
            return self._root

        tem_node = None
        # 没有子节点 将当前节点置为None
        if not search_node.left and not search_node.right:
            pass
        # 只有一个节点 将当前节点替换为它的子节点
        elif not search_node.left and search_node.right:
            tem_node = search_node.right
        elif search_node.left and not search_node.right:
            tem_node = search_node.left
        else:
            # 两个节点都有值 这时候有两种选择，左分支的最大值 或者 右分支的最小值
            # 这里选择右分支最小值策略
            rirht_min_node = search_node.right
            right_min_pre_node = None
            while rirht_min_node.left:
                right_min_pre_node = rirht_min_node
                rirht_min_node = rirht_min_node.left
            tem_node = rirht_min_node

            if right_min_pre_node:
                # 右分支的最小值节点，不是删除元素的子节点，左边肯定是没有节点了，右边的节点需要替换它的位置
                right_min_pre_node.left = tem_node.right
                tem_node.right = search_node.right
            # 右分支的最小值节点，是删除元素的子节点，直接提上来就可以.处理右侧要避免环。
            tem_node.left = search_node.left

        if pre_node:
            if pre_node.left and pre_node.left.val == search_node.val:
                pre_node.left = tem_node
            else:
                pre_node.right = tem_node
        else:
            self._root = tem_node
        return self._root

    def asc_order_list(self) -> List[int]:
        "中序遍历"
        ans = []
        if not self._root:
            return ans
        node_stack = []
        root_node = self._root
        while root_node or len(node_stack) > 0:
            if root_node:
                node_stack.append(root_node)
                root_node = root_node.left
            else:
                cur_node = node_stack.pop()
                ans.append(cur_node.val)
                root_node = cur_node.right
        return ans

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


def main():
    search_tree = BinarySearchTree()
    search_tree.insert(50)
    search_tree.insert(30)
    search_tree.insert(70)
    search_tree.insert(40)
    search_tree.insert(60)
    search_tree.insert(80)
    print(f"层序遍历={search_tree.level_order_list()}")
    print("删除50")
    search_tree.remove(50)
    print(f"层序遍历={search_tree.level_order_list()}")
    print(f"中序遍历={search_tree.asc_order_list()}")
    # search_tree.insert(8)
    # search_tree.insert(12)
    # search_tree.insert(4)
    # search_tree.insert(6)
    # search_tree.insert(2)
    # search_tree.insert(10)
    # search_tree.insert(14)
    # search_tree.insert(1)
    # search_tree.insert(3)
    # search_tree.insert(5)
    # search_tree.insert(7)
    # search_tree.insert(11)
    # search_tree.insert(9)
    # search_tree.insert(15)
    # search_tree.insert(13)
    # print(f"层序遍历={search_tree.level_order_list()}")
    # print(f"中序遍历={search_tree.asc_order_list()}")
    # search_tree.remove(1)
    # print("删除1")
    # print(f"层序遍历={search_tree.level_order_list()}")
    # print(f"中序遍历={search_tree.asc_order_list()}")
    # search_tree.remove(2)
    # print("删除2")
    # print(f"层序遍历={search_tree.level_order_list()}")
    # print(f"中序遍历={search_tree.asc_order_list()}")
    # search_tree.remove(12)
    # print("删除12")
    # print(f"层序遍历={search_tree.level_order_list()}")
    # print(f"中序遍历={search_tree.asc_order_list()}")

if __name__ == "__main__":
    main()
