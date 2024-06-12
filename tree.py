from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:

    def level_traversal(self, root: Optional[TreeNode]) -> List[int]:
        # 层序遍历 广度搜索
        ans = []
        if not root:
            return ans
        help_list = deque()
        help_list.append(root)
        while len(help_list) > 0:
            cur = help_list.popleft()
            ans.append(cur.val)
            if cur.left: 
                help_list.append(cur.left)
            if cur.right: 
                help_list.append(cur.right)
        return ans
    
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        level_node_list = []
        level_node_list.append(root)
        while len(level_node_list) > 0 :
            level_val_list = [] 
            next_level_node_list = []
            for node in level_node_list:
                level_val_list.append(node.val)
                if node.left:
                    next_level_node_list.append( node.left)
                if node.right:
                    next_level_node_list.append( node.right)
            ans.append(level_val_list)
            level_node_list = next_level_node_list
        return ans

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        # 前序遍历  中左右
        "递归写法"
        # ans = []
        # if root:
        #     self.preorder_traversal_help(root, ans)
        # return ans
        "迭代写法"
        ans = []
        if not root:
            return ans
        help_stack = []
        help_stack.append(root)
        while len(help_stack) > 0:
            cur = help_stack.pop()
            ans.append(cur.val)
            if cur.right:
                help_stack.append(cur.right)
            if cur.left:
                help_stack.append(cur.left)
        return ans

    def preorder_traversal_help(self, root: Optional[TreeNode], ans: List[int]):
        if root:
            ans.append(root.val)
        if root.left:
            self.preorder_traversal_help(root.left, ans)
        if root.right:
            self.preorder_traversal_help(root.right, ans)


def tree():
    # 初始化二叉树
    # 初始化节点
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    n6 = TreeNode(val=6)
    n7 = TreeNode(val=7)
    # 构建节点之间的引用（指针）
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    solution = Solution()
    print(f"层序遍历={solution.level_traversal(n1)}")
    print(f"层序遍历分层={solution.level_order(n1)}")
    print(f"前序遍历={solution.preorder_traversal(n1)}")


def main():
    tree()


if __name__ == "__main__":
    main()
