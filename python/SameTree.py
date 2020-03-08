# https://leetcode.com/problems/same-tree/
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.helper(p, q)
    def helper(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            if p.val == q.val:
                is_left_same = self.helper(p.left, q.left)
                is_right_same = self.helper(p.right, q.right)
                if is_left_same and is_right_same:
                    return True
            return False
        return False
