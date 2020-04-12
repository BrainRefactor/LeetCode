class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.tree_range_sum(root, L, R, 0)

    def tree_range_sum(self, node, left, right, total):
        if node is None:
            return total

        if left <= node.val <= right:
            total += node.val

            total = self.tree_range_sum(node.left, left, right, total)
            total = self.tree_range_sum(node.right, left, right, total)

        if node.val < left:
            total = self.tree_range_sum(node.right, left, right, total)

        if node.val > right:
            total = self.tree_range_sum(node.left, left, right, total)

        return total
