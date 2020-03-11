# https://leetcode.com/problems/binary-tree-preorder-traversal/
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        return self.iterative(root, nodes)
    def recursive(self, root, nodes):
        if not root:
            return []
        nodes.append(root.val)
        if root.left:
            self.recursive(root.left, nodes)
        if root.right:
            self.recursive(root.right, nodes)
        return nodes
    
    def _compute(self, node, result):
        result.append(node.val)
    
    def iterative(self, root, nodes):
        stack = []
        current = root
        while current or stack:
            if current:
                self._compute(current, nodes)
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                current = node.right
        return nodes
