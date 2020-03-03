#
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Time Complexity : O(n) as we are iterating over all the values of arrays
# Space Complexity: O(n) we are building a recursion stack

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build_helper(preorder, inorder)
    
    def build_helper(self, preorder, inorder):
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        if len(preorder) == len (inorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        
        partition = inorder.index(preorder[0])
        
        root.left = self.build_helper(preorder[1: partition+1], inorder[0: partition])
        root.right = self.build_helper(preorder[partition + 1:], inorder[partition+1:])
        
        return root