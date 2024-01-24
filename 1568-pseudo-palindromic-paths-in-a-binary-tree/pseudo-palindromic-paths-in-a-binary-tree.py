
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 0
    digits = [0]*10

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result 

    def dfs(self, root):
        if root is None:
            return

        self.digits[root.val] += 1

        if root.left is None and root.right is None:
            if self.isPalindrome():
                self.result += 1
        else:
            self.dfs(root.left)
            self.dfs(root.right)

        self.digits[root.val] -= 1

    def isPalindrome(self):
        odd = 0
        for i in range(0, 10):
            if self.digits[i] % 2 != 0:
                odd += 1

        return odd <= 1
