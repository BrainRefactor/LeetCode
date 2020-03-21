# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
#
# Time Complexity: O(n)
# Space Complexity: O(n) - recursion call stack
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        node, _ = self.helper(original, cloned, target)
        return node
    
    def helper(self, original, cloned, target):
        
        if original is None and cloned is None:
            return None, False
        
        if original.val == target.val:
            return cloned, True
        
        left_node, is_left = self.helper(original.left, cloned.left, target)
        right_node, is_right = self.helper(original.right, cloned.right, target)
        
        if is_left:
            return left_node, True
        if is_right:
            return right_node, True
        
        return None, False
