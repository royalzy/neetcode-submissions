# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        thought process
         put right = left and left = right
         FIFO BFS
        '''
        if not root:
            return None
        curr = root
        seen = deque()
        seen.append(curr)

        while seen:
            curr = seen.popleft()
            if curr.left:
                seen.append(curr.left)
            if curr.right:
                seen.append(curr.right)

            curr.left, curr.right = curr.right, curr.left

        return root
        

