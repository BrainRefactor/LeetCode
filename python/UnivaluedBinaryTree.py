#
# https://leetcode.com/problems/univalued-binary-tree/
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.helper(root, root.val)
    def helper(self, root, key):
        if root is None:
            return True
        
        if root.val == key:
            is_left_subtree = self.helper(root.left, key)
            is_right_subtree = self.helper(root.right, key)
            if is_left_subtree and is_right_subtree:
                return True
            return False
        return False
