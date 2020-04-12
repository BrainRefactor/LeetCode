class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.helper(t1, t2)

    def helper(self, node1, node2):
        if node1 is None:
            return node2

        if node2 is None:
            return node1

        node1.val += node2.val

        node1.left = self.helper(node1.left, node2.left)
        node1.right = self.helper(node1.right, node2.right)

        return node1
