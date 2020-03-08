# https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helper_iterative(root)
    def helper(self, node):
        nodes = []
        if node is not None:
            if node.left is not None:
                self.helper(node.left, nodes)
            nodes.append(node.val)
            if node.right is not None:
                self.helper(node.right, nodes)
        return nodes       
    
    def helper_iterative(self, node):
        stack = []
        nodes = []
        current = node
        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                nodes.append(current.val)
                current = current.right
        return nodes
