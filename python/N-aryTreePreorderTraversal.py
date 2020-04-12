from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        results = []
        return self.helper(root, results)

    def helper(self, node, results):
        if node:
            results.append(node.val)
            for children in node.children:
                self.helper(children, results)
        return results
