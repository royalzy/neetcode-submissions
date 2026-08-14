# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:       
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left + right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))



        '''
        thought process

        find max depth of left and max depth of right
        diameter = 1 + max depth of left and max depth of right
        return max(diameter)
        '''
        