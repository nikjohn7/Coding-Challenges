class Solution:
    res=[]
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        s=''
        if root.left:
            self.sumNumbers()