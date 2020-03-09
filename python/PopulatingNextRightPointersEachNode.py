# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 
# Time Complexity: O(n)
# Space Complexity: O(n)


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        return self.helper(root)
    def helper(self, root):
        node = root
        queue = deque([])
        
        current_level = -1
        
        previous = None
        queue.append((node, 0))
        
        while queue:
            node, level = queue.popleft()
            if current_level < level:
                node.next = None
                current_level = level
                previous = node
            else:
                node.next = previous
                previous = node
            if node.right and node.left:
                queue.append((node.right, level+1))
                queue.append((node.left, level+1))
        
        return root
