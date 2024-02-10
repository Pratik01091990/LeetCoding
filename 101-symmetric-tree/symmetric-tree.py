# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_sym(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            return(t1.val == t2.val and is_sym(t1.left,t2.right) and is_sym(t2.left, t1.right))

        if root:
            return is_sym(root.left,root.right)
