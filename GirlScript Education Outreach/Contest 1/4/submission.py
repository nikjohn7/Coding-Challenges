""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      
"""
MAXIMUM=429496729
MINIMUM=-429496729
def check_binary_search_tree_(node): 
    return (isBST(node, MINIMUM, MAXIMUM)) 

def isBST(node, mini, maxi):
      
    # An empty tree is BST 
    if node is None: 
        return True
  
    # False if this node violates min/max constraint 
    if node.data < mini or node.data > maxi: 
        return False
  
    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (isBST(node.left, mini, node.data -1) and
          isBST(node.right, node.data+1, maxi)) 