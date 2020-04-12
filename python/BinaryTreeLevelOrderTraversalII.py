from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        nodes_by_level = {}
        queu = deque([])

        node = root
        queu.append([node, 0])

        while queu and node:
            node, level = queu.popleft()
            if level in nodes_by_level:
                nodes_by_level[level].append(node.val)
            else:
                nodes_by_level[level] = [node.val]

            if node.left is not None:
                queu.append([node.left, level + 1])
            if node.right is not None:
                queu.append([node.right, level + 1])

        results = []
        for k, v in sorted(nodes_by_level.items(), key=lambda x: -x[0]):
            results.append(v)

        return results
