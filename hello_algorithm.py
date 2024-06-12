from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        # 前序遍历  中左右
        "递归写法"
        # ans = []
        # if root:
        #     self.preorder_traversal_help(root, ans)
        # return ans
        "迭代写法"
        ans = []
        help_stack = deque()
        help_stack.append(root)
        while len(help_stack) > 0:
            cur = help_stack.pop()
            if cur:
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
    print(solution.preorder_traversal(n1))


def main():
    tree()


if __name__ == "__main__":
    main()
