#
# https://leetcode.com/problems/validate-binary-search-tree/
#
# Time Complexity: O(N)
# Space Complexity: O(N)
#


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution:
    def isValid(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, lower, upper):
        if node is None:
            return True

        value = node.value

        #
        # starting from the root node:
        # 1. the left subtree highest value should be <= root value
        # 2. the right subtree lowest value should be >= root value
        # otherwise its not a valid BST
        # we'll do the above recursively for all the subtrees
        #

        if value <= lower or value >= upper:
            return False
        #
        # we'll check recursively for the left subtree
        #
        if not self.helper(node.left, lower, value):
            return False
        #
        # similarly we'll check for the right subtree - recursively
        #

        if not self.helper(node.right, value, upper):
            return False

        #
        # if everything went fine then that mean the tree is valid BST
        #

        return True


if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(6)

    node4 = TreeNode(7)
    node5 = TreeNode(11)

    # root: 5
    # 4
    node1.left = node2
    # 6
    node1.right = node3
    # 7
    node3.right = node4
    # 8
    node4.right = node5

    ans = Solution().isValid(node1)
    print(ans)
