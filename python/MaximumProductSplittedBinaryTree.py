class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        tree_total = 0
        nodes = []
        tree_total += self.dfs(root, nodes)

        product_max = float('-inf')

        #
        # iterate over the nodes each having `total` property
        #

        for node in nodes:
            product = (tree_total - node.total) * node.total
            product_max = max(product, product_max)

        product_max = product_max % 1000000007
        return product_max

    def dfs(self, node, nodes) -> int:
        if node is None:
            return 0

        total = node.val + self.dfs(node.left, nodes) + self.dfs(node.right, nodes)

        #
        # adding a property `total` to node - which I will use later
        #

        node.total = total
        nodes.append(node)
        return total
