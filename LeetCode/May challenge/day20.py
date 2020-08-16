class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = []
        self.check(root, count)
        return count[k-1]
        
    def check(self, node, count):
        if not node:
            return
        
        self.check(node.left, count)
        count.append(node.val)
        self.check(node.right, count)