# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def order(self, root):
        if not root:
            return []

        fifo = deque()
        res = []
        fifo.append(root)

        while fifo:
            levelsize = len(fifo)
            levelnodes = []

            for _ in range(levelsize):
                curr = fifo.popleft()
                levelnodes.append(curr.val)

                if curr.left:
                    fifo.append(curr.left)
                if curr.right:
                    fifo.append(curr.right)
            res.append(levelnodes)
        
        return res
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels = self.order(root)
        res = []
        for level in levels:
            res.append(level[-1])

        return res


        