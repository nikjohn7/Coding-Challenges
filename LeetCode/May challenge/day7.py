def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque([(root, None)])
        while q:
            n = len(q)
            parent = None
            foundone = False
            for _ in range(n):
                node, par = q.popleft()
                if node.val==x or node.val==y:
                    if not foundone:
                        foundone = True
                        parent = par
                    else: return parent!=par
                if node.right:
                    q.append((node.right, node))
                if node.left:
                    q.append((node.left, node))
        return False