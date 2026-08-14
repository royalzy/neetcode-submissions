# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''thought process
        bfs
        fifo'''
        if not root:
            return []

        fifo = deque()
        fifo.append(root)
        res = []

        while fifo:
            level_size = len(fifo)
            current_level_nodes = []

            for _ in range(level_size):
                curr = fifo.popleft()
                current_level_nodes.append(curr.val)

                if curr.left:
                    fifo.append(curr.left)
                if curr.right:
                    fifo.append(curr.right)
                
            res.append(current_level_nodes)

        return res

        # fifo = deque()
        # fifo.append(root)
        # curr = fifo.popleft()
        # fifo.append(0)
        # res = []
        # layer = 0

        # while curr:
        #     res[layer].append([curr.val])

        #     if curr.left:
        #         fifo.append(curr.left)

        #     if curr.right:
        #         fifo.append(curr.right)

        #     curr = fifo.popleft()
        #     if curr == 0:
        #         fifo.append(0)
        #         layer += 1
        #         curr = fifo.popleft()
            
        #     else: 
        #         curr = fifo.popleft()


