# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 
# Time Complexity: O(n)
# Space Complexity: O(n)
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from collections import OrderedDict

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        return self.helper(root)
    def helper(self, root):
        level_order_nodes = OrderedDict()
        queu = deque([])
        queu.append((root, 0))
        
        while queu:
            node, level = queu.popleft()
            nodes = level_order_nodes.get(level, [])
            value = node.val
            nodes.append(value)
            level_order_nodes[level] = nodes
            if node.left:  
                queu.append((node.left, level+1))
            if node.right:
                queu.append((node.right, level+1))
        return [v for v in level_order_nodes.values()]
