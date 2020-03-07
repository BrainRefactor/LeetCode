# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# 
# Time Complexity: O(n)
# Space Complexity: O(level)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum = {}
        queu = deque([])
        
        node = root
        level = 1
        queu.append((node, level))
        
        while queu:
            node, level = queu.popleft()
            if level in level_sum:
                level_sum[level] += node.val
            else:
                level_sum[level] = node.val
            
            if node.left is not None:
                queu.append((node.left, level+1))
            if node.right is not None:
                queu.append((node.right, level+1))
        
        return max(level_sum, key=level_sum.get)
