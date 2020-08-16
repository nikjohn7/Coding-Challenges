class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and val<root.val:
            return self.searchBST(root.left,val)
        elif root and val>root.val:
            return self.searchBST(root.right,val)
        return root