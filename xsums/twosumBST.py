 #!/usr/bin/python3   

from operator import truediv


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(self, root: TreeNode, k: int) -> bool:
   def recurse(self, root):
      if not root:
         return False
      hm = {}
      if k - root.val in hm:
         return True
      else:
         hm[root.val] = True
         return recurse(root.left) or recurse(root.right)
         
   return recurse(root)

