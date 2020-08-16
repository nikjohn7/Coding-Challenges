class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count=0
        if root is None:
            return 0
        else:
            count+=1
        # if root.left:
        #     count+=1
        # if root.right:
        #     count+=1
        count+=(self.countNodes(root.left)+self.countNodes(root.right))
        return count